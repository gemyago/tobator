from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from api.handlers.openai import audio, chat_completions, embeddings, images, models

app = FastAPI(
    title="OpenAI-Compatible API Proxy",
    description="API gateway proxying OpenAI-compatible endpoints.",
    version="0.1.0",
)


@app.get("/", tags=["Root"])
async def root(request: Request):
    """
    Root endpoint for health check or welcome.
    """
    # Try to get correlation_id from request.state, then from header, else "N/A"
    correlation_id = getattr(request.state, "correlation_id", None)
    if correlation_id is None:
        correlation_id = request.headers.get("X-Request-ID", "N/A")
    return JSONResponse({
        "message": "Hello, world!",
        "correlation_id": correlation_id,
    })


# Register OpenAI endpoint routers
app.include_router(chat_completions.router)
app.include_router(embeddings.router)
app.include_router(models.router)
app.include_router(images.router)
app.include_router(audio.router)

