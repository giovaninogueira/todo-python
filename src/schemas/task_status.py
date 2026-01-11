from pydantic import BaseModel, Field

from enums.status_task import StatusTask

class TaskStatusDTO(BaseModel):
    status: StatusTask