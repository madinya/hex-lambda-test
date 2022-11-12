from datetime import datetime

from pydantic import BaseModel


class NoteSubmit(BaseModel):
    client_id: int
    description: str


class Note(NoteSubmit):
    id: int
    created_date: datetime
