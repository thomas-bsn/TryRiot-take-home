from fastapi import APIRouter, Request, HTTPException
from services.EncryptionService import encrypt_payload
from services.DecryptionService import decrypt_payload
from services.SignatureService import sign_payload, verify_signature

router = APIRouter()

@router.post("/encrypt")
async def encrypt(request: Request):
    data = await request.json()
    result = encrypt_payload(data)
    return result

@router.post("/decrypt")
async def decrypt(request: Request):
    data = await request.json()
    return decrypt_payload(data)

@router.post("/sign")
async def sign(request: Request):
    data = await request.json()
    return sign_payload(data)

@router.post("/verify")
async def verify(request: Request):
    payload = await request.json()
    signature = payload.get("signature")
    data = payload.get("data")
    if not signature or not data:
        raise HTTPException(status_code=400, detail="Missing signature or data")
    if verify_signature(data, signature):
        return "", 204
    raise HTTPException(status_code=400, detail="Invalid signature")