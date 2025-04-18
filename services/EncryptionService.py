import base64
import json

def encrypt_payload(data):
    encrypted = {}
    for key, value in data.items():
        if isinstance(value, (dict, list)):
            value_str = json.dumps(value)
        else:
            value_str = str(value)
        encrypted[key] = base64.b64encode(value_str.encode()).decode()
    return encrypted
