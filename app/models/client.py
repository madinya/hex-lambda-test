import datetime
from typing import Optional, List

from pydantic import BaseModel

from app.models.project import Project


class ClientBase(BaseModel):
    name: str
    status: int
    industry: int


class Client(ClientBase):
    id: int
    created_date: datetime.datetime
