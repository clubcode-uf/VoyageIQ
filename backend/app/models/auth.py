from pydantic import BaseModel, EmailStr, Field

class RegisterRequest(BaseModel):
    name: str 
    email: EmailStr
    password: str = Field(min_length=8)

class AuthResponse(BaseModel):
    token: str
    user: dict

