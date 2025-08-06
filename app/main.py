from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.routes import include_all_routes

app = FastAPI(title="FastAPI Microservice")

# 👇 CORS settings
origins = [
    "http://localhost:3000",  # React dev server (default)
    "http://localhost:3001",  # your current port
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 👈 frontend URLs allowed to access this API
    allow_credentials=True,
    allow_methods=["*"],     # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],     # Allow all headers
)

# Root route to prevent 404 on "/"
@app.get("/", include_in_schema=False)
def root():
    return {"message": "Welcome to CATALYST FastAPI Microservice 🎉"}


# Include all your modular routes
include_all_routes(app)
