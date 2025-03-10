from fastapi import APIRouter, Depends, HTTPException, status
from schemas import CreateTodo, EditData, CreateUser
from crud import create_todo, get_all_todo, get_todo_by_id, delete_todo, edit_todo, get_user_by_username, create_user
from fastapi.security import OAuth2PasswordRequestForm

route = APIRouter()

@route.post("/todos")
async def add_todo(create_td: CreateTodo):
    createtd = create_todo(create_td)
    return createtd
    
@route.get("/")
async def get_todos():
    return get_all_todo()
 
 
@route.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    todo = get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo
        
@route.delete("/todos/{todo_id}")
async def remove_todo(todo_id: int):
    todo = delete_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    else:
        return {"message": "Todo deleted succesfully"}
    
    
@route.put("/todos/{todo_id}")
async def update_todo(todo_id:int, edit_data:EditData):
    update_td = edit_todo(todo_id, edit_data)
    if update_td is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    else: 
        return {"message": "You todo updated succesfully !!!",
                "todo": update_td  
                }

@route.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm=Depends()):
    user = get_user_by_username(form_data.username)
    if not user or not user.verify_password(form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": user.username, "token_type": "bearer"}

@route.post("/register")
async def register_user(user_data: CreateUser):
    user = create_user(user_data)
    return user