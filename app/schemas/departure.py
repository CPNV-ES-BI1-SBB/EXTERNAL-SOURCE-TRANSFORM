from pydantic import BaseModel
from typing import Optional, List
from app.schemas.train import Train

class Departure(BaseModel):
    departureStationName: str
    departureTime: str
    destinationStationName: str
    platform: str
    sector: Optional[str]
    train: Train
    viaStationNames: List[str]
