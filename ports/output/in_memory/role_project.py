from datetime import datetime

from ports.output.in_memory.base_in_memory import InMemoryPort
from models import Role


class RolePort(InMemoryPort):
    data_source = [Role(id=1, name="", description="", created_date=datetime.now())]
