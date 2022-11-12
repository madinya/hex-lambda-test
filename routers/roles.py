from typing import List, Optional

from fastapi import APIRouter, Response
from models import Role, Contact, RoleSubmit, Note
from ports.input import RoleInputPort
from utils import ResponseError
roles_router = APIRouter(tags=["roles"])


@roles_router.get("/roles/", name="all_roles", response_model=List[Role])
async def get() -> List[Role]:
    return RoleInputPort.get_all()


@roles_router.get("/roles/{project_id}", name="get_client", response_model=Role)
async def get(project_id: int) -> Optional[Role]:
    try:
        return RoleInputPort.get_by_id(project_id)
    except ResponseError as re:
        return Response(content=re.error_msg, status_code=re.status_code)


@roles_router.post("/roles/", response_model=Role)
async def post(client: RoleSubmit) -> Role:
    return RoleInputPort.create(client)


@roles_router.put("/roles/{item_id}", response_model=Role)
async def put(item_id: int, project: RoleSubmit) -> Role:
    project = Role(id=item_id)
    RoleInputPort.update(project)


@roles_router.get("/roles/{int}/notes", response_model=List[Note])
async def get() -> List[Note]:
    return RoleInputPort.get_all()
