from pydantic import BaseModel, EmailStr

class LoginInput(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str ="bearer"
    first_name: str 
    
class RefreshTokenRequest(BaseModel):
    refresh_token: str
