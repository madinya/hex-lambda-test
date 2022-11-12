from typing import List

import fastapi
from fastapi import APIRouter
from app.ports.input.client import ClientInputPort
from app.models.client import Client, ClientSubmit
from app.models.contact import Contact
from app.models.notes import Note
from app.utils.ResponseError import ResponseError

clients_router = APIRouter(tags=["clients"])


@clients_router.get("/clients/", name="all_clients", response_model=List[Client])
async def get():
    return ClientInputPort.get_all()


@clients_router.get("/clients/{client_id}", name="get_client", response_model=Client)
async def get(client_id: int):
    try:
        return ClientInputPort.get_by_id(client_id)
    except ResponseError as re:
        return fastapi.Response(content=re.error_msg, status_code=re.status_code)


@clients_router.post("/clients/", response_model=Client)
async def post(client: ClientSubmit):
    return ClientInputPort.create(client.__dict__)


@clients_router.put("/clients/{client_id}", response_model=Client)
async def put(client_id: int, client: ClientSubmit):
    client = Client(client_id=client_id)
    ClientInputPort.update()


@clients_router.get("/clients/{client_id}/contacts", response_model=List[Contact])
async def get_contacts(client_id: int):
    return ClientInputPort.get_contacts_by_client(client_id)


@clients_router.get("/clients/{client_id}/notes", response_model=List[Note])
async def get_notes(client_id: int):
    return ClientInputPort.get_notes_by_client(client_id)


@clients_router.get("/clients/{client_id}/projects", response_model=List[Note])
async def get_projects(client_id: int):
    return ClientInputPort.get_notes_by_client(client_id)
