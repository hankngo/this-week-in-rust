import jwt
import os
import datetime

from dotenv import load_dotenv
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

load_dotenv()

def generate_signed_jwt():
    """
    Generates a JWT: 
    Encodes and signs the payload using RS256 and the private RSA key, forming a base64-url encoded header, payload, and signature. 
    Then returns it.
    """
    AUTHORIZED_MEMBER_ID = os.getenv('AUTHORIZED_MEMBER_ID', "") # the member id that owns the OAuth Client
    CLIENT_KEY = os.getenv('CLIENT_KEY', "")
    pem_bytes = (os.getenv('PRIVATE_KEY', "")).encode()
    PRIVATE_KEY = serialization.load_pem_private_key(
        pem_bytes, password=None, backend=default_backend()
    )
    payload = {
        "sub": AUTHORIZED_MEMBER_ID,
        "iss": CLIENT_KEY,
        "aud": "api.meetup.com",
        "exp": (datetime.datetime.utcnow() + datetime.timedelta(hours=24)).timestamp()
    }
    return jwt.encode(
        payload=payload, 
        key=PRIVATE_KEY, 
        algorithm="RS256"
    )