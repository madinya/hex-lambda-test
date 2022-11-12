from typing import List, Optional

from fastapi import APIRouter, Response
from utils import ResponseError
from models.contact import Contact, ContactSubmit
from ports.input.contact import ContactInputPort

contacts_router = APIRouter(tags=["contacts"])


@contacts_router.get("/contacts/", name="get_contacts", response_model=List[Contact])
async def get():
    return ContactInputPort.get_all()


@contacts_router.get("/contacts/{contact_id}", name="get_contact", response_model=Contact)
async def get(contact_id: int):
    try:
        return ContactInputPort.get_by_id(contact_id)
    except ResponseError as re:
        return Response(content=re.error_msg, status_code=re.status_code)


@contacts_router.post("/contacts/", response_model=Contact)
async def post(contact: ContactSubmit):
    return ContactInputPort.create(contact.__dict__)


@contacts_router.put("/contacts/{item_id}", response_model=Contact)
async def put(item_id: int, contact: ContactSubmit):
    contact = Contact(id=item_id)
    ContactInputPort.update(contact.__dict__)


@contacts_router.get("/contacts/{int}/notes", response_model=List[Contact])
async def get() -> List[Contact]:
    return ContactInputPort.get_all()
