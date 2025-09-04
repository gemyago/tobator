import logging
import logging.config
import os
import sys
from typing import Any, Dict

import orjson
import structlog
from asgi_correlation_id import correlation_id
from structlog.processors import TimeStamper

try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None  # colorama is optional in production

def orjson_dumps(obj, *, default):
    # structlog expects a function with this signature for JSON serialization
    return orjson.dumps(obj, default=default).decode()

def get_correlation_id(logger, method_name, event_dict):
    """
    structlog processor to inject the current correlation_id into every log record.
    """
    cid = correlation_id.get()
    if cid:
        event_dict["correlation_id"] = cid
    return event_dict

def setup_logging(is_json_logs: bool = False) -> None:
    """
    Configure both stdlib logging and structlog for the application.

    Args:
        is_json_logs (bool): If True, use JSON output (production).
                             If False, use colored, human-readable output (development).
    """
    # Common logging config for all environments
    logging_config: Dict[str, Any] = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {},
        "handlers": {},
        "root": {
            "level": "INFO",
            "handlers": ["default"],
        },
        "loggers": {
            # Silence overly verbose loggers if needed
            "uvicorn.error": {"level": "INFO"},
            "uvicorn.access": {"level": "INFO"},
        },
    }

    if is_json_logs:
        # Production: JSON logs, UTC ISO 8601 timestamps, single line per event
        logging_config["formatters"]["json"] = {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.processors.JSONRenderer(serializer=orjson_dumps),
            "foreign_pre_chain": [
                get_correlation_id,
                structlog.stdlib.add_log_level,
                TimeStamper(fmt="iso", utc=True, key="timestamp"),
            ],
        }
        logging_config["handlers"]["default"] = {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "json",
        }
    else:
        # Development: colored, key=value, local time
        logging_config["formatters"]["console"] = {
            "()": structlog.stdlib.ProcessorFormatter,
            "processor": structlog.dev.ConsoleRenderer(colors=True),
            "foreign_pre_chain": [
                get_correlation_id,
                structlog.stdlib.add_log_level,
                TimeStamper(fmt="iso", utc=False, key="timestamp"),
            ],
        }
        logging_config["handlers"]["default"] = {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "console",
        }

    # Apply stdlib logging config
    logging.config.dictConfig(logging_config)

    # structlog processor chain
    structlog_processors = [
        get_correlation_id,  # Add correlation_id to every log
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        TimeStamper(fmt="iso", utc=is_json_logs, key="timestamp"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ]

    structlog.configure(
        processors=structlog_processors,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    # Optionally print a message on startup
    logger = structlog.get_logger()
    logger.info(
        "Logging configured",
        mode="json" if is_json_logs else "console",
        env=os.environ.get("APP_ENV", "development"),
    )
