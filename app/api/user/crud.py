from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.api.user.models import User
from app.api.user.schemas import UserCreate
from app.api.auth.password_utils import hash_password

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()

async def create_user(db: AsyncSession, user_data: UserCreate):
    user = User(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        school_name=user_data.school_name,
        grade=user_data.grade,
        dob=user_data.dob,
        email=user_data.email,
        hashed_password=hash_password(user_data.password)
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
