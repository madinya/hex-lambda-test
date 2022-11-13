from typing import Optional

from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):

    __tablename__: Optional[str] = None

    class Meta:
        pass

    class Config:
        orm_mode: bool = True

    @classmethod
    def __init_subclass__(cls, environment: Optional[str] = None) -> None:
        if not getattr(cls, '__tablename__', None):
            prefix = environment.lower() if environment else ''
            base_name = f'{prefix}-{cls.__name__.lower()}'
            tablename = f'{base_name}s' if getattr(cls.Meta, 'pluralize', False) else base_name
            setattr(cls, '__tablename__', tablename)
