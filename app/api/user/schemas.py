from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class UserCreate(BaseModel):
    first_name:str
    last_name:str
    school_name: Optional[str]
    grade: Optional[str]
    email: EmailStr
    password: str
    dob: Optional[date]
    
    
class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    school_name: Optional[str]
    grade: Optional[str]
    email: EmailStr
    dob: Optional[date]

    model_config = {
    "from_attributes": True
    }
