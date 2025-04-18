import base64
import json

from services.strategies.Base64Encryption import Base64Encryption

encryptor = Base64Encryption()

def encrypt_payload(data):
    return 
    {
        k: encryptor.encrypt(json.dumps(v) if isinstance(v, (dict, list)) else str(v))
        for k, v in data.items()
    }
