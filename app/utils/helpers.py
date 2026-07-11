from app.engine.decision import decide_action

merchant = {}

trigger = {
    "type":"festival"
}

print(decide_action(merchant,trigger))