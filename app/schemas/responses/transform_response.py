from pydantic import BaseModel
from typing import List
from app.schemas.departure import Departure

class TransformResponse(BaseModel):
    name: str
    departures: List[Departure]