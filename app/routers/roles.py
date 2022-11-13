from typing import List, Optional

from fastapi import APIRouter, Response
from app.models import Role, Contact, RoleSubmit, Note
from app.ports.input import RoleInputPort
from app.utils import ResponseError

roles = APIRouter()


@roles.get("/", name="all_roles", response_model=List[Role])
async def get() -> List[Role]:
    return RoleInputPort.get_all()


@roles.post("/", response_model=Role)
async def post(role: RoleSubmit):
    return RoleInputPort.create(role.__dict__)


@roles.put("/{role_id}", response_model=Role)
async def put(role_id: int, role: RoleSubmit):
    role = Role(id=role_id)
    RoleInputPort.update(role.__dict__)


@roles.delete("/{role_id}", response_model=Role)
async def delete(role_id: int):
    RoleInputPort.delete(role_id)


@roles.get("/{role_id}", name="get individual role", response_model=Role)
async def get(role_id: int):
    try:
        return RoleInputPort.get_by_id(role_id)
    except ResponseError as re:
        return Response(content=re.error_msg, status_code=re.status_code)


@roles.get("/{role_id}/notes", response_model=List[Note])
async def get(role_id: int) -> List[Note]:
    return RoleInputPort.get_notes_by_role(role_id)
