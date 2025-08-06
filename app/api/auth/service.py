from app.api.auth.jwt import create_access_token, create_refresh_token
from app.api.user.crud import get_user_by_email
from app.api.auth.security import verify_password
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

async def authenticate_user(db: AsyncSession, email: str, password: str):
    user = await get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access = create_access_token({"sub": user.email})
    refresh = create_refresh_token({"sub": user.email})
    return access, refresh
