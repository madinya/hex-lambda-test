from ports.input import BaseInputPort
from ports.output.in_memory.note_port import NotePort


class NoteInputPort(BaseInputPort):
    output_port = NotePort

    pass