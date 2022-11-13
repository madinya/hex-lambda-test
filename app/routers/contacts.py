from typing import List, Optional

from fastapi import APIRouter, Response
from app.utils import ResponseError
from app.models.contact import Contact, ContactSubmit
from app.ports.input.contact import ContactInputPort

contacts = APIRouter()


@contacts.get("/", name="get_contacts", response_model=List[Contact])
async def get():
    return ContactInputPort.get_all()


@contacts.post("/", response_model=Contact)
async def post(contact: ContactSubmit):
    return ContactInputPort.create(contact.__dict__)


@contacts.put("/{contact_id}", response_model=Contact)
async def put(contact_id: int, contact: ContactSubmit):
    contact = Contact(contact_id=contact_id)
    ContactInputPort.update(contact.__dict__)


@contacts.delete("/{contact_id}", response_model=Contact)
async def delete(contact_id: int):
    ContactInputPort.delete(contact_id)


@contacts.get("/{contact_id}", name="get_contact", response_model=Contact)
async def get(contact_id: int):
    try:
        return ContactInputPort.get_by_id(contact_id)
    except ResponseError as re:
        return Response(content=re.error_msg, status_code=re.status_code)


@contacts.get("/{contact_id}/notes", response_model=List[Contact])
async def get(contact_id: int) -> List[Contact]:
    return ContactInputPort.get_all()
