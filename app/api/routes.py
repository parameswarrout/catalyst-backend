from fastapi import FastAPI
from app.api.user.router import router as user_router
from app.api.auth.router import router as auth_router

def include_all_routes(app: FastAPI):
    app.include_router(user_router, prefix="/users", tags=["Users"])
    app.include_router(auth_router, prefix="/auth", tags=["Auth"])
