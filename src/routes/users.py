import bcrypt
from fastapi import APIRouter, Depends, HTTPException
from models.user import UserEntity
from schemas.user import UserDTO as User
from sqlalchemy.orm import Session
from config.dps import get_db
from repositories.user import UserRepository
from loguru import logger
import requests

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/")
def create_user(user: User, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    user_existing = user_repo.find_by_email(user.email)

    if user_existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    address = get_address_by_zip(user.zip_code)
    password_hash = bcrypt.hashpw(
        password=user.password.encode("utf-8"), salt=bcrypt.gensalt()
    ).decode("utf-8")

    user_entity = UserEntity(
        name=user.name,
        email=user.email,
        zip_code=user.zip_code,
        address=address.get("logradouro", ""),
        password_hash=password_hash,
    )
    user_created = user_repo.create(user_entity)

    logger.info(f"User created with email: {user_created.email}")

    return {"data": user_created}


def get_address_by_zip(zip_code: str):
    response = requests.get(f"https://viacep.com.br/ws/{zip_code}/json/")

    if response.status_code != 200 or "erro" in response.json():
        raise HTTPException(status_code=400, detail="Invalid zip code")

    return response.json()
