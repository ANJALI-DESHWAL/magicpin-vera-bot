def build_rationale(action, merchant, trigger):

    offer = merchant.get(
        "offer",
        "available offer"
    )

    sales_drop = merchant.get(
        "sales_drop",
        0
    )

    name = merchant.get(
        "name",
        "Merchant"
    )

    festival = trigger.get(
        "festival",
        "festival"
    )


    if action == "festival_campaign":

        return (
            f"{festival} opportunity detected. "
            f"{name} has an active offer '{offer}', "
            f"so this is a good time to promote it."
        )


    if action == "boost_sales":

        return (
            f"Sales dropped by {sales_drop}%. "
            f"Since {name} has an active offer '{offer}', "
            f"promotion can help bring more customers."
        )


    if action == "capture_demand":

        return (
            f"Demand spike detected. "
            f"Promoting '{offer}' now can capture nearby customer interest."
        )


    if action == "customer_recall":

        return (
            f"Customer recall opportunity detected. "
            f"Sending '{offer}' can help bring previous customers back."
        )


    if action == "improve_listing":

        rating = merchant.get(
            "rating",
            "low"
        )

        return (
            f"Merchant rating is {rating}. "
            f"Improving listing quality can increase customer trust."
        )


    return (
        "No urgent growth signal detected. "
        "General recommendation provided."
    )