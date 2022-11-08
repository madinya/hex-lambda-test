from fastapi import FastAPI
from routers import clients_router, notes_router, contacts_router, index

app = FastAPI()

app.include_router(index)
app.include_router(notes_router)
app.include_router(contacts_router)
app.include_router(clients_router)
