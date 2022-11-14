from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.ports.input import ClientInputPort
templates = Jinja2Templates('app/templates')

index = APIRouter()
MENU = [
    {"description": "Clients", "url": ""},
    {"description": "Contacts", "url": ""},
    {"description": "Projects", "url": ""},
    {"description": "Roles", "url": ""},
]

@index.get("/view/home", include_in_schema=False)
async def get(request: Request):
    result = [ item.__dict__ for item in ClientInputPort.get_all()]
    return templates.TemplateResponse('index.html', {'request': request,
                                                     'menus': MENU,
                                                     'clients': result})



@index.get("/", include_in_schema=False)
async def get(request: Request):
    return {"app": "clients app",
            "version": "0.1",
            "backend": "lambda"}
