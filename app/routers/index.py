from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

index = APIRouter()


@index.get("/")
async def get(request: Request):
    return {"app": "clients app",
            "version": "0.1",
            "backend": "lambda"}
