from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory = 'templates')

@app.get("/")
def read_root():
    return {"message": "API is working"}

@app.get("/hello", response_class = HTMLResponse)
def get_message_hello(name: str = None, request: Request = None):
    return templates.TemplateResponse(
        request = request,
        name = "hello.html",
        context = {"name": name, "default_names": ["Piter", "John"]}
    )

@app.get("/calculation", response_class=HTMLResponse)
def get_sum(a: int|float = None, b: int|float = None, operation: str = None, request: Request = None):
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
        context = {"summ": answers}
    )

