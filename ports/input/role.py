from ports.input import BaseInputPort
from ports.output.in_memory import RolePort


class RoleInputPort(BaseInputPort):
    output_port = RolePort

    pass
