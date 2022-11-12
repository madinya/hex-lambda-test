import datetime

from pydantic import BaseModel


class ProjectSubmit(BaseModel):
    name: str
    inv_code: str
    description: str
    status: int
    client_id: int
    reporting_to: int
    owner: str


class Project(ProjectSubmit):
    id: int
    created_date: datetime.datetime
