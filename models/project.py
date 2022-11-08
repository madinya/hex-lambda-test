import datetime

from pydantic import BaseModel


class ProjectSubmit(BaseModel):
    name: str
    description: str


class Project(ProjectSubmit):
    id: int
    created_date: datetime.datetime
