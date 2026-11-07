from fastapi import FastAPI, Request, APIRouter
from fastapi.params import Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from app.data.auth import check_credentials, login_user, get_current_user, logout_user
from app.templates import templates


router = APIRouter()

@router.get("/login", response_class=HTMLResponse)
def student_login(request: Request, error: str | None = None):
    
    return templates.TemplateResponse(
        request = request,
        name = "login.html",
        context = {"error": error}
    )
    
@router.post("/api/login")
def login(request: Request, username: str = Form(), password: str = Form()):
    
    if not check_credentials(username, password):
        
        return RedirectResponse("/login?error=wrong", status_code=302)
    
    response = RedirectResponse("/students", status_code = 302)
    login_user(response, username)
    
    return response
    
@router.post("/api/logout", response_class=RedirectResponse)
def logout(request: Request):
    
    response = RedirectResponse("/login", status_code = 302)
    logout_user(response, request)
    
    return response
