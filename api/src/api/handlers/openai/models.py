from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/v1/models", status_code=status.HTTP_501_NOT_IMPLEMENTED)
async def list_models():
    """
    Stub for OpenAI-compatible models listing endpoint.
    """
    return JSONResponse(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        content={
            "error": {
                "message": "This endpoint is not yet implemented.",
                "type": "not_implemented_error",
                "code": None,
            }
        },
    )
