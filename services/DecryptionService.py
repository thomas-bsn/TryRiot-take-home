import base64
import json

def decrypt_payload(data):
    result = {}
    for key, value in data.items():
        try:
            decoded = base64.b64decode(value).decode()
            try:
                result[key] = json.loads(decoded)  # obj ou liste ?
            except json.JSONDecodeError:
                if decoded.isdigit():
                    result[key] = int(decoded)
                else:
                    result[key] = decoded
        except Exception:
            result[key] = value
    return result
