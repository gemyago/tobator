import logging
import sys

def setup_logging():
    """
    Set up logging for the FastAPI application.
    - Logs to stdout.
    - Includes timestamp, log level, logger name, and message.
    - Sets root logger to INFO by default.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        stream=sys.stdout,
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    # Optionally, reduce verbosity of third-party loggers
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.error").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)