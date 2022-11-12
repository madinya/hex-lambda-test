from fastapi import FastAPI
from app.routers import clients_router, notes_router, contacts_router, index, roles_router, project_router

app = FastAPI()

app.include_router(index)
app.include_router(notes_router)
app.include_router(contacts_router)
app.include_router(clients_router)
app.include_router(roles_router)
app.include_router(project_router)
