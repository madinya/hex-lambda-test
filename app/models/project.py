import datetime

from pydantic import BaseModel


class ProjectBase(BaseModel):
    name: str
    inv_code: str
    description: str
    status: int
    client_id: int
    reporting_to: int
    owner: str


class Project(ProjectBase):
    id: int
    created_date: datetime.datetime
