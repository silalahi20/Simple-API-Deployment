api_keys = {
    "e54d4431-5dab-474e-b71a-0db1fcb9e659": "EUrRSnwrBlbAE4aLQ7iibR98EB0GkZjGMqLQwubFVRs",
}

users = {
    "EUrRSnwrBlbAE4aLQ7iibR98EB0GkZjGMqLQwubFVRs": {
        "name": "ParMusic",
        "message" : "Semoga TST dapat A. A for Aminn"
    }
}

def check_api_key(api_key: str):
    return api_key in api_keys

def get_user_from_api_key(api_key: str):
    return users[api_keys[api_key]]
