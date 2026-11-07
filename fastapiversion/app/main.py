from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.students import router as student_router
from app.seed import init_db


app = FastAPI()

init_db() 

app.include_router(auth_router)
app.include_router(student_router)
