message_history = {}


def is_suppressed(merchant_id, suppression_key):
    """
    Check if this message was already sent.
    """
    if merchant_id not in message_history:
        return False

    return suppression_key in message_history[merchant_id]


def save_message(merchant_id, suppression_key):
    """
    Save sent message suppression key.
    """
    if merchant_id not in message_history:
        message_history[merchant_id] = set()

    message_history[merchant_id].add(suppression_key)