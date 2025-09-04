
from fastapi import FastAPI
from .logging_config import setup_logging
import logging
from contextlib import asynccontextmanager

setup_logging()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("FastAPI application startup")
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    logger.info("Received request for root endpoint")
    return {"Hello": "World"}
