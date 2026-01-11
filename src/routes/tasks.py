from fastapi import APIRouter, Depends, HTTPException
from enums.status_task import StatusTask
from models.tasks import TaskEntity
from repositories.task import TaskRepository
from schemas.task import TaskDTO
from sqlalchemy.orm import Session
from config.dps import get_db
from loguru import logger
from middlewares.auth_middleware import auth_middleware
from schemas.task_status import TaskStatusDTO

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/")
def create_task(task: TaskDTO, db: Session = Depends(get_db), user_id=Depends(auth_middleware)):    
    task_repository = TaskRepository(db)
    task_entity = TaskEntity(
        title=task.title,
        description=task.description,
        status=StatusTask.BACKLOG,
        user_id=user_id
    )
    task_created = task_repository.create(task_entity)
    
    logger.info(f"Task created with ID: {task_created.id} for User ID: {user_id}")
    
    return {
        'data': task_created
    }
    
@router.put("/{task_id}/status")
def update_status_task(task_id: int, task_dto: TaskStatusDTO, db: Session = Depends(get_db), user_id=Depends(auth_middleware)):    
    task_repository = TaskRepository(db)
    task = task_repository.find_by_id_and_user(task_id=task_id, user_id=user_id)
    
    if not task:
        logger.error(f"Task with ID: {task_id} not found for User ID: {user_id}")
        raise HTTPException(status_code=404, detail="Task not found")
    
    task_repository.update_status(task=task, new_status=task_dto.status)
    logger.info(f"Task updated with ID: {task.id} for User ID: {user_id}")
    
    return {
        'data': 'Status updated successfully'
    }