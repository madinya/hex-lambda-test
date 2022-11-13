from uuid import uuid4
from datetime import datetime
from app.utils.mock import get_random_string, get_random_int
from app.models import ClientBase

def mock_client_base() -> ClientBase:
    values = {
        "id": get_random_int(),
        "name": get_random_string(),
        "status": get_random_int(), 
        "industry": get_random_int(),
        "created_date": datetime.now()
    }
    
    return ClientBase(**values)