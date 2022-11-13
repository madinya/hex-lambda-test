from typing import Any, Optional, List
from app.ports.output.base_output import BaseOutputPort


class BaseInputPort:
    output_port: Optional[BaseOutputPort] = None

    @classmethod
    def get_by_id(cls, _id: Any) -> Any:
        return cls.output_port.get_by_id(_id)

    @classmethod
    def get_all(cls) -> List[Any]:
        return cls.output_port.get_all()

    @classmethod
    def create(cls, entry: dict) -> List[Any]:
        return cls.output_port.create(entry)

    @classmethod
    def update(cls, new_values: dict) -> Any:
        try:
            _id = new_values.pop('_id', None)
            if not _id:
                return None, 'Error: No id was provided for update'
            return cls.output_port.update(_id, new_values), None
        except RuntimeError as ex:
            return None, str(ex)

    @classmethod
    def delete(cls, _id: Any) -> Any:
        return cls.output_port.delete(_id)
