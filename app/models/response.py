from pydantic import BaseModel
from app.models.tick import TickRequest
from app.engine.compose import compose
from app.storage.memory import get_merchant


class ComposeResponse(BaseModel):
    message: str
    cta: str
    send_as: str
    suppression_key: str
    rationale: str  