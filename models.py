# định nghĩa model dữ liệu
from warnings import deprecated
from sqlmodel import SQLModel, Field, table
from datetime import datetime
import pytz
from passlib.context import CryptContext




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ho_chi_minh_tz = pytz.timezone('Asia/Ho_Chi_Minh')

def get_vietnam_tz():
    return datetime.now(ho_chi_minh_tz)


class Todo (SQLModel, table=True):
    id : int = Field(default=None, primary_key=True)
    title : str = Field(max_length=255)
    completed : bool = Field(default=False)
    todo_date : datetime = Field(default_factory=get_vietnam_tz)
    
class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username : str = Field(unique=True, index=True)
    full_name : str
    email : str
    hashed_password : str
    disabled : bool = Field(default=False)
    
    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.hashed_password)
    
    def set_password(self, password: str):
        self.hashed_password = pwd_context.hash(password)