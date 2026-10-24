from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db_api import get_student_by_id
from db_api import get_students
from data.model import Student


app = FastAPI()

templates = Jinja2Templates(directory = 'templates')

@app.get("/")
def read_root():
    return {"message": "API is working"}

@app.get("/hello", response_class = HTMLResponse)
def get_message_hello(request: Request, name: str = "Гость"):
    return templates.TemplateResponse(
        request = request,
        name = "hello.html",
        context = {"name": name, "default_names": ["Piter", "John"]}
    )

@app.get("/say-hello", response_class = HTMLResponse)
def say_hello(request: Request):
    return templates.TemplateResponse(
        request = request,
        name = "say-hello.html",
        context = {},
    )
    
@app.get("/calculation", response_class=HTMLResponse)
def get_sum(request: Request, a: int|float = None, b: int|float = None, operation: str = "+"):
    answers = []
    
    if a is not None and b is not None:
        match operation:
            case "+":
                result = a + b
                
            case "-":
                result = a - b
                
            case "*":
                result = a * b
                
            case "/":
                result = a / b
                
            case "//":
                result = a // b
            
            case "**":
                result = a ** b
                
        answers = [result]
                
        
    return templates.TemplateResponse(
        request = request,
        name = "calculation.html",
        context = {
            "a": a,
            "b": b,
            "operation": operation,
            "answers": answers,
        },
    )

@app.get("/student/{id}", response_class=HTMLResponse)
def student(id: int, request: Request):
    student = get_student_by_id(id)
    
    return templates.TemplateResponse(
        request = request,
        name = "student.html",
        context = {"student": student},
    )
    
@app.get("/students", response_class=HTMLResponse)
def students(request: Request):
    students = get_students()
    
    return templates.TemplateResponse(
        request = request,
        name = "students.html",
        context = {"students": students},
    )

@app.get("/stat", response_class=HTMLResponse)
def stat(request: Request):
    students = get_students()
    
    return templates.TemplateResponse(
        request = request,
        name = "stat.html",
        context = {"students": students},
    )
