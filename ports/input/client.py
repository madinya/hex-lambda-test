from typing import List

from models.contact import Contact
from models.notes import Note
from ports.input.base_input import BaseInputPort
from ports.output.in_memory.client_port import ClientPort


class ClientInputPort(BaseInputPort):
    output_port = ClientPort

    def get_contacts_by_client(self) -> List[Contact]:
        self.get_all()

    def get_notes_by_client(self) -> List[Note]:
        self.get_all()
