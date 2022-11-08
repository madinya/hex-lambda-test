from typing import List

from fastapi import APIRouter

from models.contact import Contact
from ports.input.contact import ContactInputPort
contacts_router = APIRouter(tags=["contacts"])


@contacts_router.get("/contacts/", name="get_contacts", response_model=List[Contact])
async def get():
    return ContactInputPort.get_all()
