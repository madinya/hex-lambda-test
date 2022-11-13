from typing import List

from fastapi import APIRouter, Response

from app.models.notes import Note, NoteSubmit
from app.ports.input import NoteInputPort
from app.utils import ResponseError

notes = APIRouter()


@notes.get("/", name="all_notes", response_model=List[Note])
async def get():
    return NoteInputPort.get_all()


@notes.get("/{note_id}", name="get_note", response_model=Note)
async def get(note_id: int):
    try:
        return NoteInputPort.get_by_id(note_id)
    except ResponseError as re:
        return Response(content=re.error_msg, status_code=re.status_code)


@notes.post("/", response_model=Note)
async def post(note: NoteSubmit):
    return NoteInputPort.create(note.__dict__)


@notes.put("/{note_id}", response_model=Note)
async def put(note_id: int, note: NoteSubmit):
    note = Note(id=note_id)
    NoteInputPort.update(note.__dict__)


@notes.delete("/{note_id}", response_model=Note)
async def delete(note_id: int):
    NoteInputPort.delete(note_id)
