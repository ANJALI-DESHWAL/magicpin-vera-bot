from app.engine.decision import decide_action
from app.engine.templates import MESSAGE_TEMPLATES
from app.engine.rationale import build_rationale
from app.engine.suppression import generate_suppression_key
from app.engine.category_rules import CATEGORY_RULES
from app.engine.merchant_analyzer import analyze_merchant
from app.engine.trigger_analyzer import analyze_trigger


def build_message(category, action, merchant, trigger, customer=None):

    offer = merchant["offer"]
    name = merchant["name"]
    drop = merchant["sales_drop"]
    festival = trigger.get("festival", "Upcoming Festival")

    # Customer based personalization
    if customer:

        customer_name = customer.get("name", "")
        relationship = customer.get("relationship", "").lower()

        if relationship == "repeat":
            return (
                f"😊 Invite your repeat customer {customer_name} "
                f"with your '{offer}' offer."
            )

    category = category.lower()

    # ---------------- DENTIST ----------------
    if category == "dentist":

        if action == "boost_sales":
            return (
                f"🦷 Appointments are down by {drop}%. "
                f"Promote '{offer}' to nearby patients?"
            )

        elif action == "festival_campaign":
            return (
                f"🦷 {festival} is coming. "
                f"Promote '{offer}' before the festive rush."
            )

    # ---------------- RESTAURANT ----------------
    elif category == "restaurant":

        if action == "capture_demand":
            return (
                f"🍽️ Food searches are increasing nearby. "
                f"Highlight '{offer}' now."
            )

        elif action == "boost_sales":
            return (
                f"🍽️ Orders are down by {drop}%. "
                f"Promote '{offer}' today?"
            )

    # ---------------- SALON ----------------
    elif category == "salon":

        if action == "boost_sales":
            return (
                f"💇 Weekend bookings are down by {drop}%. "
                f"Promote '{offer}'."
            )

    # ---------------- GYM ----------------
    elif category == "gym":

        if action == "customer_recall":
            return (
                f"🏋️ Invite inactive members back with "
                f"'{offer}'."
            )

    # ---------------- PHARMACY ----------------
    elif category == "pharmacy":

        if action == "festival_campaign":
            return (
                f"💊 Demand may increase during {festival}. "
                f"Promote '{offer}'."
            )

    # Default template
    template = MESSAGE_TEMPLATES[action]

    return template.format(
        merchant_name=name,
        festival=festival,
        offer=offer,
        drop=drop
    )


def compose(category, merchant, trigger, customer=None):

    merchant_info = analyze_merchant(merchant)

    trigger_info = analyze_trigger(trigger)

    action = decide_action(
        merchant_info,
        trigger_info
    )

    rules = CATEGORY_RULES.get(
        category.lower(),
        CATEGORY_RULES["restaurant"]
    )

    message = build_message(
        category,
        action,
        merchant_info,
        trigger_info,
        customer
    )

    return {

        "message": message,

        "cta": rules["cta"],

        "send_as": rules["send_as"],

        "suppression_key": generate_suppression_key(
            merchant.get("id", "merchant"),
            action
        ),

        "rationale": build_rationale(
            action,
            merchant_info,
            trigger_info
        )
    }