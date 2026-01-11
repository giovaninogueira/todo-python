from datetime import datetime, timedelta, timezone
from typing import Union
from fastapi import APIRouter, Depends, HTTPException
from config.dps import get_db
from models.user import UserEntity
from repositories.user import UserRepository
from schemas.login import LoginDTO
from sqlalchemy.orm import Session
import bcrypt
import jwt
import os

router = APIRouter(prefix='/auth', tags=['auth'])

@router.post('/login')
def login(login_dto: LoginDTO, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user = user_repository.find_by_email(login_dto.email)
    
    validate_user(user, login_dto)
    token = create_token(user)
    
    return {'message': 'Login successful', 'token': token}

def create_token(user: UserEntity) -> str:
    expiration_time = datetime.now(timezone.utc) + timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    payload = {
        "user_id": user.id,
        "email": user.email,
        "exp": expiration_time
    }
    return jwt.encode(payload, os.getenv("SECRET_JWT"), algorithm=os.getenv("ALGORITHM"))

def validate_user(user: Union[UserEntity, None], login_dto: LoginDTO):
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    if not bcrypt.checkpw(login_dto.password.encode('utf-8'), user.password_hash.encode('utf-8')):
        raise HTTPException(status_code=401, detail="Invalid email or password")