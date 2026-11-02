from fastapi import FastAPI, Request
from fastapi.params import Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from calculations import calculate
from db_api import get_student_by_id
from db_api import get_students
from data.auth import check_credentials, login_user, get_current_user, logout_user
from data.model import Student
from stat_calc import score_stats


app = FastAPI()

templates = Jinja2Templates(directory = 'templates')

@app.get("/")

def require_user(request: Request):
    
    user = get_current_user(request)

    if user is None:
        return RedirectResponse("/login", status_code = 302)
    
    return user

def read_root():

    return {"message": "API is working"}

@app.get("/hello", response_class = HTMLResponse)
def get_message_hello(request: Request, name: str = "Гость"):
    
    user = require_user(request)
        
    if isinstance(user, RedirectResponse):
        return user 
        
    return templates.TemplateResponse(
        request = request,
        name = "hello.html",
        context = {"name": name, "default_names": ["Piter", "John"]}
    )

@app.get("/say-hello", response_class = HTMLResponse)
def say_hello(request: Request):
    
    user = require_user(request)
        
    if isinstance(user, RedirectResponse):
        return user 
        
    return templates.TemplateResponse(
        request = request,
        name = "say-hello.html",
        context = {},
    )
    
@app.get("/calculation", response_class=HTMLResponse)
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

@app.get("/student/{id}", response_class=HTMLResponse)
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
    
@app.get("/students", response_class=HTMLResponse)
def students(request: Request):
    
    students = get_students()
    user = require_user(request)
    
    if isinstance(user, RedirectResponse):
        return user 
        
    return templates.TemplateResponse(
        request = request,
        name = "students.html",
        context = {"students": students},
    )

@app.get("/stat", response_class=HTMLResponse)
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

@app.get("/login", response_class=HTMLResponse)
def student_login(request: Request, error: str | None = None):
    
    return templates.TemplateResponse(
        request = request,
        name = "login.html",
        context = {"error": error}
    )
    
@app.post("/api/login")
def login(request: Request, username: str = Form(), password: str = Form()):
    
    if not check_credentials(username, password):
        
        return RedirectResponse("/login?error=wrong", status_code=302)
    
    response = RedirectResponse("/students", status_code = 302)
    login_user(response, username)
    
    return response
    
@app.post("/api/logout", response_class=RedirectResponse)
def logout(request: Request):
    
    response = RedirectResponse("/login", status_code = 302)
    logout_user(response, request)
    
    return response
