import datetime
from typing import Optional, List

from pydantic import BaseModel

from app.models.project import Project


class ClientSubmit(BaseModel):
    name: str
    status: int
    industry: int
    projects: Optional[List[Project]]


class Client(ClientSubmit):
    id: int
    created_date: datetime.datetime
