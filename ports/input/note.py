from ports.input.base_input import BaseInputPort
from ports.output.in_memory.note_port import NotePort


class ContactInputPort(BaseInputPort):
    output_port = NotePort

    pass
