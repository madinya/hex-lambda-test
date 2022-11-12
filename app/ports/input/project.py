from app.ports.input import BaseInputPort
from app.ports.output.in_memory import ProjectPort, NotePort


class ProjectInputPort(BaseInputPort):
    output_port = ProjectPort
    note_port = NotePort

    @classmethod
    def get_notes_by_project(cls, client_id: int):
        cls.note_port.get_by_id(client_id)
