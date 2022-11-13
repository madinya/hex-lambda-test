from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import clients_router, notes_router, contacts_router, index, roles_router, project_router

app = FastAPI(openapi_url=f'/stage/openapi.json', docs_url=f'/stage/docs')
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(index)
app.include_router(notes_router)
app.include_router(contacts_router)
app.include_router(clients_router)
app.include_router(roles_router)
app.include_router(project_router)
