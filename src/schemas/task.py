from pydantic import BaseModel, Field

class TaskDTO(BaseModel):
    title: str = Field(..., example="Buy groceries", max_length=100)
    description: str = Field(..., example="Buy milk, eggs, and bread", max_length=300)