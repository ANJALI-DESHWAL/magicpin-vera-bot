merchant_store = {}

customer_store = {}

category_store = {}

def save_context(scope, context_id, version, payload):

    stores = {
        "merchant": merchant_store,
        "customer": customer_store,
        "category": category_store
    }

    store = stores[scope]

    if context_id in store:

        if version <= store[context_id]["version"]:
            return False

    store[context_id] = {
        "version": version,
        "payload": payload
    }

    return True

def get_merchant(merchant_id):

    return merchant_store.get(merchant_id)