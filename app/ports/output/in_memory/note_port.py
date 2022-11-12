from datetime import datetime

from app.ports.output.in_memory.base_in_memory import InMemoryPort
from app.models.notes import Note


class NotePort(InMemoryPort):
    data_source = [Note(id=1, client_id=1, description="Note", created_date= datetime.now()),
                   Note(id=2, client_id=2, description="Note 1", created_date=datetime.now())]
