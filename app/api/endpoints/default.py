from fastapi import APIRouter, HTTPException, status

from app.api.schemas import DefaultSchema

router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Check API status",
    response_model=DefaultSchema,
)
@router.get(
    "/status",
    status_code=status.HTTP_200_OK,
    summary="Check API status",
    response_model=DefaultSchema,
)
def default_response():
    """Check API status"""

    if not router:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="GrindNode API is not available",
        )

    return {"status": True}
