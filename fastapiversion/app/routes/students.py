from fastapi import FastAPI, Request, APIRouter
from fastapi.params import Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from app.calculations import calculate
from app.db_api import get_student_by_id
from app.db_api import get_students
from app.data.auth import check_credentials, login_user, get_current_user, logout_user
from app.models.students import Students
from app.stat_calc import score_stats
from app.routes.auth import router as auth_router
from app.templates import templates
from app.database import SessionLocal


router = APIRouter()

@router.get("/")
def require_user(request: Request):
    
    user = get_current_user(request)

    if user is None:
        return RedirectResponse("/login", status_code = 302)
    
    return user

def read_root():

    return {"message": "API is working"}

@router.get("/hello", response_class = HTMLResponse)
def get_message_hello(request: Request, name: str = "Гость"):
    
    user = require_user(request)
        
    if isinstance(user, RedirectResponse):
        return user 
        
    return templates.TemplateResponse(
        request = request,
        name = "hello.html",
        context = {"name": name, "default_names": ["Piter", "John"]}
    )

@router.get("/say-hello", response_class = HTMLResponse)
def say_hello(request: Request):
    
    user = require_user(request)
        
    if isinstance(user, RedirectResponse):
        return user 
        
    return templates.TemplateResponse(
        request = request,
        name = "say-hello.html",
        context = {},
    )
    
@router.get("/calculation", response_class=HTMLResponse)
def get_sum(request: Request, a: int|float = None, b: int|float = None, operation: str = "+"):
    
    user = require_user(request)
        
    if isinstance(user, RedirectResponse):
        return user 
    
    result = calculate(a, b, operation)

    return templates.TemplateResponse(
        request = request,
        name = "calculation.html",
        context = {
            "a": a,
            "b": b,
            "operation": operation,
            "result": result,
        },
    )

@router.get("/student/{id}", response_class=HTMLResponse)
def student(id: int, request: Request):
    
    student = get_student_by_id(id)
    user = require_user(request)
        
    if isinstance(user, RedirectResponse):
        return user 
        
    return templates.TemplateResponse(
        request = request,
        name = "student.html",
        context = {"student": student},
    )
    
@router.get("/students", response_class=HTMLResponse)
def students(request: Request):
    
    #students = get_students()
    user = require_user(request)
    
    if isinstance(user, RedirectResponse):
            return user 
        
    db = SessionLocal()
    
    try:
        students = db.query(Students).order_by(Students.id).all()
        
        return templates.TemplateResponse(
            request = request,
            name = "students.html",
            context = {"students": students},
        )
    finally:
        db.close()

@router.get("/stat", response_class=HTMLResponse)
def stat(request: Request):
    
    user = require_user(request)
        
    if isinstance(user, RedirectResponse):
        return user 

    students = get_students()
    scores543list = score_stats(students)
    
    return templates.TemplateResponse(
        request = request,
        name = "stat.html",
        context = {"students": students, "scores543list": scores543list},
    )
