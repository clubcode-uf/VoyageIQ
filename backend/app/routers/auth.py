from fastapi import APIRouter, HTTPException, status
from app.models.auth import RegisterRequest
from app.utils.db import db
import bcrypt
import os
from jose import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv

router = APIRouter()

load_dotenv()
SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 

@router.post("/register", response_model=AuthResponse)
async def register(data: RegisterRequest):
    existing_user = await db.user.find_unique(where={"email":data.email})
    if existing_user is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
    hashed_password = bcrypt.hashpw(data.password.encode('utf-8'),bcrypt.gensalt())

    new_user = await db.user.create(data={
        "name": data.name,
        "email": data.email,
        "passwordHash": hashed_password.decode('utf-8'),
    })

    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": str(new_user.id),
        "exp": expire
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "token": token,
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        },
        "message": "User registered successfully!"
    }

