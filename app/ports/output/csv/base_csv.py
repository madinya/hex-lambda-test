from typing import Any
from ports.output.base_output import BaseOutputPort


class CsvPort(BaseOutputPort):
    @classmethod
    def get_all(cls):
        return [{"response": "Retrieving data from csv"}, {"response": "Retrieving another data from csv"}]

    @classmethod
    def get_by_id(cls, _id: Any):
        return {"response": "Retrieving data from csv"}

    @classmethod
    def create(cls, entry: dict):
        return {"response": "Creating data from csv"}

    @classmethod
    def update(cls, _id: Any, new_values: dict):
        return {"response": "Updating data from csv"}
