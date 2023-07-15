from pydantic import BaseModel, EmailStr, Field


class CreateUserDTO(BaseModel):
    first_name: str = Field(min_length=3, max_length=25)
    last_name: str = Field(min_length=3, max_length=25)
    email: EmailStr
    user_name: str = Field(min_length=8, max_length=25)
    password: str = Field(min_length=8, max_length=25)


class UserDto(BaseModel):
    id: int
    first_name: str = Field(min_length=3, max_length=25)
    last_name: str = Field(min_length=3, max_length=25)
    user_name: str = Field(min_length=8, max_length=25)
