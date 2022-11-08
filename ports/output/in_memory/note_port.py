from datetime import datetime

from ports.output.in_memory.base_in_memory import InMemoryPort
from models.notes import Note


class NotePort(InMemoryPort):
    data_source = [
        Note(id=1, client_id=1, description="Hello world!", created_date=datetime.now()),
        Note(id=2, client_id=2, description="Ya me cansé", created_date=datetime.now()),
        Note(id=3, client_id=1, description="No se que hacer", created_date=datetime.now())]
    pass
