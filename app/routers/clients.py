from typing import List

import fastapi
from fastapi import APIRouter
from app.ports.input.client import ClientInputPort
from app.models import Client, ClientBase, Contact ,Note, Project
from app.utils.ResponseError import ResponseError

clients = APIRouter()


@clients.get("/", name="all_clients", response_model=List[Client])
async def get():
    return ClientInputPort.get_all()


@clients.post("/", response_model=Client)
async def post(client: ClientBase):
    return ClientInputPort.create(client)


@clients.put("/{client_id}", response_model=Client)
async def put(client_id: int, client: ClientBase):
    client = Client(client_id=client_id)
    return ClientInputPort.update()


@clients.delete("/{client_id}", response_model=Client)
async def delete(client_id: int):
    return ClientInputPort.delete(client_id)


@clients.get("/{client_id}", name="get_client", response_model=Client)
async def get(client_id: int):
    try:
        model = Client
        response = ClientInputPort.get_by_id(client_id)
        return response
    except ResponseError as re:
        return fastapi.Response(content=re.error_msg, status_code=re.status_code)


@clients.get("/{client_id}/contacts", response_model=List[Contact])
async def get_contacts(client_id: int):
    return ClientInputPort.get_contacts_by_client(client_id)


@clients.get("/{client_id}/notes", response_model=List[Note])
async def get_notes(client_id: int):
    return ClientInputPort.get_notes_by_client(client_id)


@clients.get("/{client_id}/projects", response_model=List[Project])
async def get_projects(client_id: int):
    return ClientInputPort.get_projects_by_client(client_id)
