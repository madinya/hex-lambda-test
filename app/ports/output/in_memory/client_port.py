from datetime import datetime
from typing import List, Optional

from app.models.client import Client, ClientSubmit
from app.models.project import Project
from app.ports.output.in_memory.base_in_memory import InMemoryPort
from app.utils.ResponseError import ResponseError


class ClientPort(InMemoryPort):
    data_source = [Client(id=1, name="Client 1", status=1,  industry=1,
                          projects=[
                              Project(id=1,
                                      name="P1",
                                      inv_code="",
                                      description="",
                                      status=1,
                                      client_id=1,
                                      reporting_to=1,
                                      owner="",
                                      created_date=datetime.now()),
                              Project(id=2,
                                      name="P1",
                                      inv_code="",
                                      description="",
                                      status=1,
                                      client_id=1,
                                      reporting_to=1,
                                      owner="",
                                      created_date=datetime.now())],
                          created_date=datetime.now()),
                   Client(id=2, name="Client 2", status=2, industry=1, created_date=datetime.now()),
                   Client(id=3, name="Client 3", status=1, industry=2, created_date=datetime.now()),
                   Client(id=4, name="Client 4", status=1, industry=3, created_date=datetime.now())]

    @classmethod
    def create(cls, entry: ClientSubmit) -> Client:
        client = Client(id=len(cls.data_source) + 1, name=entry.name, status=entry.status, created_date=datetime.now())
        cls.data_source.append(client)
        return client

    @classmethod
    def get_by_id(cls, _id: id) -> Optional[Client]:
        for item in cls.data_source:
            if item.id == _id:
                return item
        raise ResponseError(error_msg="Client not found", status_code=404)
