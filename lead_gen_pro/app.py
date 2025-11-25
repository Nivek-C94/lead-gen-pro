from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from lead_gen_pro.ui.routers import router as ui_router

app = FastAPI(title="Lead Gen Pro", version="0.1.0")

# Mount static and templates
app.mount("/static", StaticFiles(directory="lead_gen_pro/static"), name="static")
templates = Jinja2Templates(directory="lead_gen_pro/templates")

app.include_router(ui_router)


@app.get("/")
def index():
    return {"message": "Lead Gen Pro API running"}
