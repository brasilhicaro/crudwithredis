from _datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


def generate_uuid() -> str:
    return str(uuid4())


def generate_date() -> str:
    return str(datetime.now())


class Product(BaseModel):
    id: str = Field(default_factory=generate_uuid)
    name: str
    price: float
    date: str = Field(default_factory=generate_date)
