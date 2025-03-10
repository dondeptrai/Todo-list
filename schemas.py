# xác định schemas cho request và response
from sqlmodel import SQLModel, Field
from datetime import datetime
from models import get_vietnam_tz

class CreateTodo(SQLModel):
    title : str = Field(..., max_length=255, description="Write you to do")
    completed : bool = Field(default=False, description="Task completed status")

class EditData(SQLModel):
    title : str = Field(..., max_length=255, description="Write you to do")
    completed : bool = Field(default=False, description="Task completed status")
    todo_date : datetime = Field(default_factory=get_vietnam_tz)
    
class CreateUser(SQLModel):
    username: str
    full_name: str
    email: str
    hashed_password: str