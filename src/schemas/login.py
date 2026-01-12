from pydantic import BaseModel, EmailStr, Field


class LoginDTO(BaseModel):
    email: EmailStr = Field(..., example="john.doe@example.com")
    password: str = Field(..., example="strongpassword123")
