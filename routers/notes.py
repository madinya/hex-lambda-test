from typing import List

from fastapi import APIRouter

from models.notes import Note
from ports.input.note import ContactInputPort
notes_router = APIRouter(tags=["notes"])


@notes_router.get("/notes/", name="get_notes", response_model=List[Note])
async def get():
    return ContactInputPort.get_all()
