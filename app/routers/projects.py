from typing import List, Optional

from fastapi import APIRouter, Response
from app.models import Project, ProjectBase, Note
from app.ports.input import ProjectInputPort
from app.utils import ResponseError

project = APIRouter()


@project.get("/", name="all_projects", response_model=List[Project])
async def get() -> List[Project]:
    return ProjectInputPort.get_all()


@project.post("/", response_model=Project)
async def post(client: ProjectBase):
    return ProjectInputPort.create(client.__dict__)


@project.put("/{project_id}", response_model=Project)
async def put(project_id: int, project: ProjectBase):
    project = Project(id=project_id)
    ProjectInputPort.update(project.__dict__)


@project.delete("/{project_id}", response_model=Project)
async def delete(project_id: int):
    ProjectInputPort.delete(project_id)


@project.get("/{project_id}", name="get_project", response_model=Project)
async def get(project_id: int):
    try:
        return ProjectInputPort.get_by_id(project_id)
    except ResponseError as re:
        return Response(content=re.error_msg, status_code=re.status_code)


@project.get("/{project_id}/notes", response_model=List[Note])
async def get(project_id: int) -> List[Note]:
    return ProjectInputPort.get_by_id(project_id)
