from typing import List
from pydantic import BaseModel


class TransformRequest(BaseModel):
    objects_URI: List[str]