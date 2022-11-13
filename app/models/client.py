import datetime

from pydantic import BaseModel


class ClientBase(BaseModel):
    name: str
    status: int
    industry: int


class Client(ClientBase):
    id: int
    created_date: datetime.datetime
