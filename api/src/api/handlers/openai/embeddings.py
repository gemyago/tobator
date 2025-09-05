from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/v1/embeddings", status_code=status.HTTP_501_NOT_IMPLEMENTED)
async def create_embedding(request: Request):
    """
    Stub for OpenAI-compatible embeddings endpoint.
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
