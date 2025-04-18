import hmac
import hashlib
import json

SECRET_KEY = b"thomasboissonthomasboissonthomasboissonthomasboisson" 
# La meilleure pratique serait d'utiliser un .env ou un service de gestion de secrets comme Vault/Azure Key Vault/AWS Secrets Manager etc..

def sign_payload(data):
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":"))
    signature = hmac.new(SECRET_KEY, canonical.encode(), hashlib.sha256).hexdigest()
    return 
    { 
        "signature": signature 
    }

def verify_signature(data, signature):
    expected = sign_payload(data)["signature"]
    return hmac.compare_digest(expected, signature)
