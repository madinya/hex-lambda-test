from ports.input import BaseInputPort
from ports.output.in_memory.note_port import NotePort


class ProjectInputPort(BaseInputPort):
    output_port = NotePort

    pass
