from app.ports.input import BaseInputPort
from app.ports.output.in_memory import ClientPort, ContactPort, NotePort, ProjectPort


class ClientInputPort(BaseInputPort):
    output_port = ClientPort
    contact_port = ContactPort
    note_port = NotePort
    project_port = ProjectPort

    @classmethod
    def get_contacts_by_client(cls, client_id: int):
        cls.contact_port.get_by_id(client_id)

    @classmethod
    def get_notes_by_client(cls, client_id: int):
        cls.note_port.get_by_id(client_id)

    @classmethod
    def get_projects_by_client(cls, client_id: int):
        cls.project_port.get_by_id(client_id)
