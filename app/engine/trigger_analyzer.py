def analyze_trigger(trigger):

    return {
        "type": trigger.get("type", "general"),
        "priority": trigger.get("priority", "medium"),
        "festival": trigger.get("festival", ""),
        "reason": trigger.get("reason", "")
    }