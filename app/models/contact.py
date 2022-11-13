import datetime

from pydantic import BaseModel


class ContactBase(BaseModel):
    client_id: int
    name: str
    email: str
    phone: str
    position: str
    location: str
    time_zone: int
    is_main: bool
    status: int


class Contact(ContactBase):
    id: int
    created_date: datetime.datetime
