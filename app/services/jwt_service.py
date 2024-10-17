import jwt
from app.validators.claim_validator import validate_claims

SECRET_KEY = "your-secret-key"

def validate_jwt(token: str):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        validate_claims(decoded_token)
        return {"status": "Token is valid"}
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")
