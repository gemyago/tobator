import time

import structlog
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response

# Use structlog logger for structured logging
logger = structlog.get_logger(__name__)

class HTTPLogMiddleware(BaseHTTPMiddleware):
    """
    Middleware to log HTTP requests and responses, including headers.
    """
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        start_time = time.time()

        # Process the request and get the response
        response = await call_next(request)

        process_time = (time.time() - start_time) * 1000

        # Attempt to get correlation_id from request state, falling back to a header
        correlation_id = getattr(request.state, "correlation_id", "N/A")
        if correlation_id == "N/A":
            correlation_id = request.headers.get("X-Request-ID", "N/A")

        # Convert headers to dict for logging
        request_headers = dict(request.headers)
        response_headers = dict(response.headers)

        log_details = {
            "method": request.method,
            "url": str(request.url),
            "status_code": response.status_code,
            "process_time_ms": f"{process_time:.2f}",
            "correlation_id": correlation_id,
            "client_ip": request.client.host if request.client else "N/A",
            "request_headers": request_headers,
            "response_headers": response_headers,
        }

        logger.info("HTTP Request Completed", http=log_details)

        return response
