import datetime

from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str
    description: str


class Role(RoleBase):
    id: int
    created_date: datetime.datetime
