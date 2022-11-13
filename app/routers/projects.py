from typing import List, Optional

from fastapi import APIRouter, Response
from app.models import Project, Contact, ProjectSubmit, Note
from app.ports.input import ProjectInputPort
from app.utils import ResponseError
project_router = APIRouter(tags=["projects"])


@project_router.get("/projects/", name="all_projects", response_model=List[Project])
async def get() -> List[Project]:
    return ProjectInputPort.get_all()


@project_router.get("/projects/{project_id}", name="get_client", response_model=Project)
async def get(project_id: int):
    try:
        return ProjectInputPort.get_by_id(project_id)
    except ResponseError as re:
        return Response(content=re.error_msg, status_code=re.status_code)


@project_router.post("/projects/", response_model=Project)
async def post(client: ProjectSubmit):
    return ProjectInputPort.create(client.__dict__)


@project_router.put("/projects/{project_id}", response_model=Project)
async def put(project_id: int, project: ProjectSubmit) :
    project = Project(id=project_id)
    ProjectInputPort.update(project.__dict__)


@project_router.get("/projects/{project_id}/notes", response_model=List[Note])
async def get(project_id: int) -> List[Note]:
    return ProjectInputPort.get_by_id(project_id)