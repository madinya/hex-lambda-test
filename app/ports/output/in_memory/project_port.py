from datetime import datetime

from app.ports.output.in_memory.base_in_memory import InMemoryPort
from app.models import Project


class ProjectPort(InMemoryPort):
    data_source = [Project(id=1,
                           name= "P1",
                           inv_code="",
                           description="",
                           status=1,
                           client_id=1,
                           reporting_to=1,
                           owner="",
                           created_date=datetime.now())]
