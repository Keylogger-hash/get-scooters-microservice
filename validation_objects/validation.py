from pydantic import BaseModel
from typing import Union, Tuple
from uuid import UUID

class Scooters(BaseModel):
    id: Union[str,UUID]
    location: tuple[float, float]
    user: str

