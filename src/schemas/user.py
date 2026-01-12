from pydantic import BaseModel, Field, EmailStr


class UserDTO(BaseModel):
    name: str = Field(..., example="John Doe", max_length=100)
    zip_code: str = Field(..., example="12345", max_length=10)
    email: EmailStr = Field(..., example="john.doe@example.com")
    password: str = Field(..., example="strongpassword123")
