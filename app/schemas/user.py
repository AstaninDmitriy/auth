import uuid
from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class RoleEnum(str, Enum):
    user: "user"
    admin = "admin"


class UserSchemas(BaseModel):
    id: Optional[uuid.UUID] = None
    email: EmailStr
    password: Optional[str] = Field(default=None, description="Не захешированный пароль пользователя")  # noqa
    hashed_password: Optional[str] = Field(default=None, description="Захешированный пароль пользователя") # noqa
    role: RoleEnum = RoleEnum.user

    class Config:
        orm_mode = True
