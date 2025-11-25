from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from lead_gen_pro.core.db import get_db

router = APIRouter()
templates = Jinja2Templates(directory="lead_gen_pro/templates")


@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html", {"request": request, "leads": []}
    )
