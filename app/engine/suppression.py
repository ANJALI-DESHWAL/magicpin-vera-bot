import hashlib


def generate_suppression_key(merchant_id, action):

    raw = f"{merchant_id}:{action}"

    return hashlib.md5(raw.encode()).hexdigest()