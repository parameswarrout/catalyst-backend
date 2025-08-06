from sqlalchemy.ext.asyncio import AsyncSession
from app.api.user.crud import get_user_by_email, create_user
from app.api.user.schemas import UserCreate

async def register_user(db: AsyncSession, user_data: UserCreate):
    existing = await get_user_by_email(db, user_data.email)
    if existing:
        raise ValueError("User already exists")
    return await create_user(db, user_data)
