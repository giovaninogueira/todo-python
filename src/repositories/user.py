from sqlalchemy.orm import Session
from models.user import UserEntity
from typing import Union

class UserRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        
    def find_by_email(self, email: str) -> Union[UserEntity, None]:
        return self.db_session.query(UserEntity).filter(UserEntity.email == email).first()
        
    def create(self, user_entity: UserEntity) -> UserEntity:
        self.db_session.add(user_entity)
        self.db_session.commit()
        self.db_session.refresh(user_entity)
        
        return user_entity