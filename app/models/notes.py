from datetime import datetime

from pydantic import BaseModel


class NoteBase(BaseModel):
    client_id: int
    description: str


class Note(NoteBase):
    id: int
    created_date: datetime
