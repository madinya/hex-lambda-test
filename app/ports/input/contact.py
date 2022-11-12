from app.ports.input import BaseInputPort
from app.ports.output.in_memory.contact_port import ContactPort


class ContactInputPort(BaseInputPort):
    output_port = ContactPort

    @classmethod
    def get_notes_by_contact(cls, client_id: int):
        cls.note_port.get_by_id(client_id)
