# schemas/user.py
import uuid
from enum import Enum
from pydantic import BaseModel, EmailStr, Field


class RoleEnum(str, Enum):
    user = "user"
    admin = "admin"


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    role: RoleEnum = RoleEnum.user


class UserOut(BaseModel):
    id: uuid.UUID
    email: EmailStr
    role: RoleEnum

    class Config:
        orm_mode = True
