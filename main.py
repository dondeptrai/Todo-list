# File chính khởi chạy api
from database import init_db
from fastapi import FastAPI
from routers import todo

app = FastAPI()

init_db()

app.include_router(todo.route)