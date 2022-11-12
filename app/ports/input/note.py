from app.ports.input import BaseInputPort
from app.ports.output.in_memory.note_port import NotePort


class NoteInputPort(BaseInputPort):
    output_port = NotePort
