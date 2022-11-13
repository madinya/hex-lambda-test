from typing import List,Any


class BaseOutputPort:

    @classmethod
    def get_all(cls) -> List[Any]:
        return [{"response": "Retrieving data"}, {"response": "Retrieving another data"}]

    @classmethod
    def get_by_id(cls, _id: Any) -> Any:
        return {"response": "Retrieving data"}

    @classmethod
    def create(cls, entry: dict) -> Any:
        return {"response": "Creating data"}

    @classmethod
    def update(cls, _id: Any, new_values: dict) -> Any:
        return {"response": "Updating data"}

    @classmethod
    def delete(cls, _id: Any) -> Any:
        return {"response": "Deleting data"}
