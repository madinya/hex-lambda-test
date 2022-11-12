from typing import List, Optional

from fastapi import APIRouter, Response
from models import Project, Contact, ProjectSubmit, Note
from ports.input import ProjectInputPort
from utils import ResponseError
project_router = APIRouter(tags=["projects"])


@project_router.get("/projects/", name="all_projects", response_model=List[Project])
async def get() -> List[Project]:
    return ProjectInputPort.get_all()


@project_router.get("/projects/{project_id}", name="get_client", response_model=Project)
async def get(project_id: int) -> Optional[Project]:
    try:
        return ProjectInputPort.get_by_id(project_id)
    except ResponseError as re:
        return Response(content=re.error_msg, status_code=re.status_code)


@project_router.post("/projects/", response_model=Project)
async def post(client: ProjectSubmit) -> Project:
    return ProjectInputPort.create(client)


@project_router.put("/projects/{item_id}", response_model=Project)
async def put(item_id: int, project: ProjectSubmit) -> Project:
    project = Project(id=item_id)
    ProjectInputPort.update(project)


@project_router.get("/projects/{int}/notes", response_model=List[Note])
async def get() -> List[Note]:
    return ProjectInputPort.get_all()
