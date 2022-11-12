from app.ports.input import BaseInputPort
from app.ports.output.in_memory import RolePort, NotePort


class RoleInputPort(BaseInputPort):
    output_port = RolePort
    note_port = NotePort

    @classmethod
    def get_notes_by_role(cls, client_id: int):
        cls.note_port.get_by_id(client_id)
