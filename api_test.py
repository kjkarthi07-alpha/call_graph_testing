
import os
import base64
import hashlib
import hmac
import jwt
from cryptography.fernet import Fernet
AWS_ACCESS_KEY_ID = "AKIA1234567890ABCDE"
 
 
JWT_SIGNING_KEY = "my-super-secret-jwt-signing-key"
JWT_REFRESH_SECRET = "refresh-secret-key-should-not-be-here"
 
 
FERNET_KEY = "z0xJYxA6Y1d7C2A7vD-EXAMPLE-KEY-K1F="
 
 
HMAC_SECRET = "payment-hmac-key-prod"
 
 
ENCODED_API_KEY = base64.b64encode(
    b"stripe-live-secret-key-prod"
).decode()
 
 
DB_PASSWORD = "Sup3rS3cretP@ssw0rd!"
 
 
SHA256_HASH = hashlib.sha256(b"hello").hexdigest()
 
 
def generate_jwt(user_id: str):
    payload = {"sub": user_id}
    return jwt.encode(
        payload,
        JWT_SIGNING_KEY,
        algorithm="HS256"
    )
 
 
def encrypt_data(data: bytes):
    f = Fernet(FERNET_KEY.encode())
    return f.encrypt(data)
 
 
EXAMPLE_TEXT = "this-is-not-a-secret-just-a-placeholder"
 
 
os.environ["PAYMENT_SECRET"] = "prod-payment-secret-key"