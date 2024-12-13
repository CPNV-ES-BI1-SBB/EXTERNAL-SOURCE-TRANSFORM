from pydantic import BaseModel


class TransformRequest(BaseModel):
    objects_URI: str