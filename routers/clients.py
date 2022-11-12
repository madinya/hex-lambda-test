from typing import List, Optional

import fastapi
from fastapi import APIRouter
from ports.input.client import ClientInputPort
from models.client import Client, ClientSubmit
from models.contact import Contact
from models.notes import Note
from utils.ResponseError import ResponseError

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
    return ClientInputPort.create(client)


@clients_router.put("/clients/{item_id}", response_model=Client)
async def put(item_id: int, client: ClientSubmit) :
    client = Client(id=item_id)
    ClientInputPort.update()


@clients_router.get("/clients/{int}/contacts", response_model=List[Contact])
async def get() :
    return ClientInputPort.get_all()


@clients_router.get("/clients/{int}/notes", response_model=List[Note])
async def get() :
    return ClientInputPort.get_all()
