from datetime import datetime
from ports.output.in_memory.base_in_memory import InMemoryPort
from models.contact import Contact


class ContactPort(InMemoryPort):
    data_source = [
        Contact(id=1, client_id=1, name="Roberto", email="rm@mail.com", position="", location="", time_zone=1,
                is_main=True,
                phone="123", status=1, created_date=datetime.now()),
        Contact(id=1, client_id=1, name="Sandra", email="sm@mail.com", position="", location="", time_zone=1,
                is_main=True,
                phone="444", status=2, created_date=datetime.now()),
        Contact(id=1, client_id=2, name="Marcela", email="mm@mail.com", position="", location="", time_zone=1,
                is_main=True,
                phone="555", status=1, created_date=datetime.now())]
