from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

index = APIRouter()
templates = Jinja2Templates(directory="templates")


@index.get("/", response_class=HTMLResponse)
async def get(request: Request):
    r = {"request": request}
    return templates.TemplateResponse("index.html", r)
