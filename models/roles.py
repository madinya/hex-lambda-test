import datetime

from pydantic import BaseModel


class RoleSubmit(BaseModel):
    name: str
    description: str


class Role(RoleSubmit):
    id: int
    created_date: datetime.datetime
