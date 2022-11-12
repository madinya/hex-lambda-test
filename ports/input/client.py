from typing import List

from models import Contact, Note
from ports.input import BaseInputPort
from ports.output.in_memory import ClientPort, ContactPort, NotePort


class ClientInputPort(BaseInputPort):
    output_port = ClientPort
    contact_port = ContactPort
    note_port = NotePort

    def get_contacts_by_client(self, client_id: int):
        self.contact_port.get_by_id(client_id)

    def get_notes_by_client(self, client_id: int):
        self.note_port.get_by_id(client_id)
