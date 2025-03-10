# kết nối và thao tác với cơ sở dữ liệu
from sqlmodel import SQLModel, create_engine
import pymysql
from models import Todo

MYSQL_URL = "mysql+pymysql://root:@localhost/todolist"

engine = create_engine(MYSQL_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)
    
