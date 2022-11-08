from typing import List, Any
from ports.output.base_output import BaseOutputPort


class InMemoryPort(BaseOutputPort):

    data_source = []

    @classmethod
    def get_all(cls) -> List[Any]:
        return cls.data_source

    @classmethod
    def get_by_id(cls, _id: Any) -> Any:
        return {"response": "Retrieving data from InMemoryPort"}

    @classmethod
    def create(cls, entry: dict) -> Any:
        return {"response": "Creating data from InMemoryPort"}

    @classmethod
    def update(cls, _id: Any, new_values: dict) -> Any:
        return {"response": "Updating data from InMemoryPort"}
