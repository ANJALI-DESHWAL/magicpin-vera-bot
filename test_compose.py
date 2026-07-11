from app.engine.compose import compose

merchant = {
    "id": "m101",
    "name": "Meera Dental",
    "offer": "Dental Checkup ₹299",
    "sales_drop": 18
}

trigger = {
    "type": "dip"
}

result = compose(
    category="dentist",
    merchant=merchant,
    trigger=trigger
)

print(result)