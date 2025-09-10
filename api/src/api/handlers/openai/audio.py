from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/v1/audio/transcriptions", status_code=status.HTTP_501_NOT_IMPLEMENTED)
async def create_audio_transcription(request: Request):
    """
    Stub for OpenAI-compatible audio transcription endpoint.
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


@router.post("/v1/audio/speech", status_code=status.HTTP_501_NOT_IMPLEMENTED)
async def create_audio_speech(request: Request):
    """
    Stub for OpenAI-compatible audio speech endpoint.
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
