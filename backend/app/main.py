from fastapi import FastAPI
from app.routers import auth

app = FastAPI()
app.include_router(auth.router, prefix="/api/auth")

@app.get("/")
async def root():
    return {"message": "VoyageIQ Backend is running"}