import datetime
from typing import Optional, List

from pydantic import BaseModel

from models.project import Project


class ClientSubmit(BaseModel):
    name: str
    projects: Optional[List[Project]]
    status: int


class Client(ClientSubmit):
    id: int
    created_date: datetime.datetime
