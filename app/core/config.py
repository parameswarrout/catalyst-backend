from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME:str
    DATABASE_URL:str
    SECRET_KEY:str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    
    class Config:
        env_file = ".env"
        extra = "ignore"
        
settings = Settings()