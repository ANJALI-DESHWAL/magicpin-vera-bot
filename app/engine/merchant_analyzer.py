def analyze_merchant(merchant):

    return {

        "name": merchant.get("name", "Merchant"),

        "category": merchant.get("category", "general"),

        "offer": merchant.get("offer", "Special Offer"),

        "rating": merchant.get("rating", 5),

        "sales_drop": merchant.get("sales_drop", 0),

        "active_offer": bool(merchant.get("offer"))
    }