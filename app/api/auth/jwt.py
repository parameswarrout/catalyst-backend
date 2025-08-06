from datetime import datetime, timedelta
from jose import jwt
from app.core.config import settings

ALGORITHM = "HS256"

def create_token(data: dict, expires_delta: timedelta, secret_key: str):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)

def decode_token(token: str, secret_key: str):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[ALGORITHM])
        return payload
    except jwt.JWTError:
        return None

def create_access_token(data: dict):
    return create_token(
        data,
        timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        settings.SECRET_KEY
    )

def create_refresh_token(data: dict):
    return create_token(
        data,
        timedelta(days=7), 
        settings.SECRET_KEY + "_refresh"
    )

def decode_refresh_token(token: str):
    return decode_token(token, settings.SECRET_KEY + "_refresh")
