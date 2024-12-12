from pydantic import BaseModel
from typing import List, Optional


class Train(BaseModel):
    g: str
    l: str

class Departure(BaseModel):
    departureStationName: str
    departuresTime: str
    destinationStationName: str
    platform: str
    sector: Optional[str]
    train: Train
    viaStationNames: List[str]

class TransformResponse(BaseModel):
    name: str
    departures: List[Departure]