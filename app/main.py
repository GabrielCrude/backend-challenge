from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.services.jwt_service import validate_jwt

app = FastAPI()

class Token(BaseModel):
    token: str

@app.post("/validate-token")
def validate_token(token: Token):
    try:
        return validate_jwt(token.token)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
