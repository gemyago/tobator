import os

import structlog
from asgi_correlation_id import CorrelationIdMiddleware, correlation_id
from fastapi import FastAPI, Request

from .logging_config import setup_logging

# Determine environment: production if APP_ENV=production, else development
APP_ENV = os.environ.get("APP_ENV", "development").lower()
IS_PRODUCTION = APP_ENV == "production"

# Configure logging before app instantiation
setup_logging(is_json_logs=IS_PRODUCTION)

app = FastAPI()

# Add correlation ID middleware
app.add_middleware(
    CorrelationIdMiddleware,
    header_name="X-Correlation-ID",  # Read from this header, or generate if missing
)

logger = structlog.get_logger()

def helper_function():
    # This function demonstrates that correlation_id is available in nested calls
    logger.info("Helper function log", helper_correlation_id=correlation_id.get())

@app.get("/")
async def root(request: Request):
    logger.info("Root endpoint called", path=request.url.path)
    logger.warning("This is a warning log", extra_data="something important")
    helper_function()
    return {"message": "Hello, world!", "correlation_id": correlation_id.get()}
