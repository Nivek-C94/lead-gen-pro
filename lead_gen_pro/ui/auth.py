from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from lead_gen_pro.config import ADMIN_USERNAME, ADMIN_PASSWORD
from starlette.middleware.sessions import SessionMiddleware

router = APIRouter()
templates = Jinja2Templates(directory="lead_gen_pro/templates")


def get_current_user(request: Request):
    return request.session.get("user")


def require_login(request: Request):
    if not get_current_user(request):
        return RedirectResponse(url="/login", status_code=303)


@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})


@router.post("/login", response_class=RedirectResponse)
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        request.session["user"] = username
        return RedirectResponse(url="/dashboard", status_code=303)
    return templates.TemplateResponse(
        "login.html", {"request": request, "error": "Invalid credentials"}
    )


@router.get("/logout", response_class=RedirectResponse)
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login", status_code=303)
