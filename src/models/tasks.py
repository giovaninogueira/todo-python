from sqlalchemy import (
    Column,
    Enum,
    ForeignKey,
    Integer,
    String,
    DateTime,
    func,
)
from sqlalchemy.orm import relationship
from config.base import Base
from enums.status_task import StatusTask


class TaskEntity(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    description = Column(String(500), nullable=True)
    status = Column(Enum(StatusTask), default=StatusTask.BACKLOG, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    user = relationship("UserEntity", back_populates="tasks")
