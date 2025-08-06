from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.api.auth.schemas import LoginInput, Token, RefreshTokenRequest
from app.api.auth.service import authenticate_user
from app.api.user.crud import get_user_by_email
from app.api.auth.jwt import decode_refresh_token, create_access_token

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(payload: LoginInput, db: AsyncSession = Depends(get_db)):
    access, refresh = await authenticate_user(db, payload.email, payload.password)
    user = await get_user_by_email(db, payload.email)
    return {
        "access_token": access,
        "refresh_token": refresh,
        "token_type": "bearer",
        "first_name": user.first_name 
    }

@router.post("/refresh", response_model=Token)
async def refresh_token(data: RefreshTokenRequest):
    payload = decode_refresh_token(data.refresh_token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    access_token = create_access_token({"sub": payload["sub"]})
    return {
        "access_token": access_token,
        "refresh_token": data.refresh_token,  
        "token_type": "bearer"
    }
