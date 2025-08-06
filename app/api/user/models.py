from sqlalchemy import Column, Integer, String, Date
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    school_name = Column(String(250), nullable=True)
    grade = Column(String(100), nullable=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    dob = Column(Date, nullable=True)
    hashed_password = Column(String(255), nullable=False)

    
    