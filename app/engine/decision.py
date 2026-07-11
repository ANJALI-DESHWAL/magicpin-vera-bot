def decide_action(merchant, trigger):

    trigger_type = trigger.get("type", "").lower()

    sales_drop = merchant.get("sales_drop", 0)
    rating = merchant.get("rating", 5)
    has_offer = merchant.get("active_offer", False)

    # Highest Priority
    if trigger_type == "festival":
        return "festival_campaign"

    if trigger_type == "spike":
        return "capture_demand"

    if trigger_type == "recall":
        return "customer_recall"

    # Sales dip
    if trigger_type == "dip":
        if has_offer:
            return "boost_sales"

    # Improve listing only if nothing else important
    if rating < 4:
        return "improve_listing"

    return "general_tip"