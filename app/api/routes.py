from fastapi import APIRouter

from app.models.context import ContextRequest
from app.models.tick import TickRequest
from app.models.reply import ReplyRequest

from app.storage.memory import save_context, get_merchant
from app.storage.history import is_suppressed, save_message

from app.engine.compose import compose

router = APIRouter()


# -----------------------------
# Health Check
# -----------------------------
@router.get("/v1/healthz")
def health():
    return {
        "status": "healthy"
    }


# -----------------------------
# Metadata
# -----------------------------
@router.get("/v1/metadata")
def metadata():
    return {
        "bot_name": "Magicpin Vera",
        "version": "1.0.0",
        "developer": "Your Name"
    }


# -----------------------------
# Store Context
# -----------------------------
@router.post("/v1/context")
def receive_context(request: ContextRequest):

    accepted = save_context(
        scope=request.scope,
        context_id=request.context_id,
        version=request.version,
        payload=request.payload
    )

    return {
        "accepted": accepted,
        "context_id": request.context_id,
        "version": request.version
    }


# -----------------------------
# Tick Endpoint
# -----------------------------
@router.post("/v1/tick")
def tick(request: TickRequest):

    merchant_record = get_merchant(request.merchant_id)

    if not merchant_record:
        return {
            "error": "Merchant not found"
        }

    merchant = merchant_record["payload"]

    category = merchant.get("category", "general")

    result = compose(
        category=category,
        merchant=merchant,
        trigger=request.trigger
    )

    # Duplicate Message Check
    if is_suppressed(
        merchant["id"],
        result["suppression_key"]
    ):
        return {
            "suppressed": True,
            "message": None,
            "reason": "Duplicate message already sent"
        }

    # Save Message History
    save_message(
        merchant["id"],
        result["suppression_key"]
    )

    return result


# -----------------------------
# Reply Endpoint
# -----------------------------
@router.post("/v1/reply")
def reply(request: ReplyRequest):

    text = request.message.lower()

    if "yes" in text:
        return {
            "status": "success",
            "reply": "Great! I'll prepare the campaign."
        }

    elif "no" in text:
        return {
            "status": "success",
            "reply": "No worries. I won't send this campaign."
        }

    elif "later" in text:
        return {
            "status": "success",
            "reply": "Sure. I'll remind you later."
        }

    else:
        return {
            "status": "success",
            "reply": "Thanks! I've recorded your response."
        }