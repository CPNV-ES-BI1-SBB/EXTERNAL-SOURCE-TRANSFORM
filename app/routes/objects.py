from fastapi import APIRouter
from app.schemas.requests import TransformRequest
from app.schemas.responses import TransformResponse

router = APIRouter()


@router.post("/transform", response_model=TransformResponse)
def transform_objects(request: TransformRequest):
    """
    # Description

    Transform objects pulled from the source and return the transformed objects.
    """
    raise NotImplementedError
