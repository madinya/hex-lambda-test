import pytest
from app.ports.input import ClientInputPort
from app.models import Client
from app.test.mocks.client import mock_client_base


def create_client() -> Client:
    client_base = mock_client_base()
    result = ClientInputPort.create(client_base.__dict__)
    return result.first()


create_client()