# Các hàm thao tác CRUD với database
from sqlmodel import Session, select
from schemas import CreateTodo, EditData, CreateUser
from models import Todo, User
from database import engine

def create_todo(todo_data: CreateTodo):  
    with Session(engine) as session:
        todo = Todo(title=todo_data.title, completed=todo_data.completed)
        session.add(todo)
        session.commit()
        session.refresh(todo)
        session.close()
        return todo


def get_all_todo():
    with Session(engine) as session:
        todos = session.exec(select(Todo)).all()
        return todos
    
    
def get_todo_by_id(todo_id: int):
    with Session(engine) as session:
        todo = session.get(Todo, todo_id)
        return todo
    
    
def delete_todo(todo_id: int):
    with Session(engine) as session:
        todo = session.get(Todo, todo_id)
        if not todo:
            return None
        else:
            session.delete(todo)
            session.commit()
            return todo
        
def edit_todo(todo_id :int, edit_data : EditData):
    with Session(engine) as session:
        todo = session.get(Todo, todo_id)
        if not todo:
            return None
        else:
            todo.title = edit_data.title if edit_data.title is not None else todo.title
            todo.completed = edit_data.completed if edit_data.completed is not None else todo.completed
            todo.todo_date =  edit_data.todo_date
            
        session.commit()
        session.refresh(todo)
        return todo
    
def create_user(user: CreateUser):
    with Session(engine) as session:
        new_user = User(username=user.username, full_name=user.full_name, email=user.email)
        new_user.set_password(user.hashed_password)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user
    
            
def get_user_by_username(username: str):
    with Session(engine) as session:
        statement = session.exec(select(User).where(User.username == username)).first()
        return statement
            
