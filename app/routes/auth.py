from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserRead
from app.models import User
from app.core.database import get_db
from app.core.security import get_password_hash

router = APIRouter


@router.post("/register", response_model="UserRead")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
