from ports.input.base_input import BaseInputPort
from ports.output.in_memory.contact_port import ContactPort


class ContactInputPort(BaseInputPort):
    output_port = ContactPort

    pass
