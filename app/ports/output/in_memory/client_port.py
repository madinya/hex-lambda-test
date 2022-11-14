from datetime import datetime
from typing import List, Optional

from app.models import Client, ClientBase, Project
from app.ports.output.in_memory.base_in_memory import InMemoryPort
from app.utils.ResponseError import ResponseError


class ClientPort(InMemoryPort):
    data_source = [Client(id=1, name="YE", status=1, industry=1, created_date=datetime.now()),
                   Client(id=2, name="GASE", status=2, industry=1, created_date=datetime.now()),
                   Client(id=3, name="Barwy Karper", status=1, industry=2, created_date=datetime.now()),
                   Client(id=4, name="Staffing Past", status=1, industry=3, created_date=datetime.now())]

    @classmethod
    def create(cls, entry: ClientBase) -> Client:
        client = Client(id=len(cls.data_source) + 1,
                        name=entry.name,
                        status=entry.status,
                        industry=entry.industry,
                        created_date=datetime.now())
        cls.data_source.append(client)
        return client

    @classmethod
    def get_by_id(cls, _id: id) -> Optional[Client]:
        for item in cls.data_source:
            if item.id == _id:
                return item
        raise ResponseError(error_msg="Client not found", status_code=404)
