from sqlalchemy.orm import Session
from models.tasks import TaskEntity

class TaskRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session
        
    def find_by_id_and_user(self, task_id: int, user_id: int) -> TaskEntity:
        return self.db_session.query(TaskEntity).filter(TaskEntity.id == task_id, TaskEntity.user_id == user_id).first()
    
    def update_status(self, task: TaskEntity, new_status: str) -> TaskEntity:
        task.status = new_status
        self.db_session.commit()
        self.db_session.refresh(task)
        
        return task
        
    def create(self, task_entity: TaskEntity) -> TaskEntity:
        self.db_session.add(task_entity)
        self.db_session.commit()
        self.db_session.refresh(task_entity)
        
        return task_entity