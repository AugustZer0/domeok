from fastapi import FastAPI, Request
import time
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from core.exception.exceptions import BaseCustomException
from api.v1.api import api_router
from core.exception.handlers import (
    custom_exception_handler,
    http_exception_handler,
    validation_exception_handler,
    system_exception_handler,
)
from core.logger import setup_logger

app = FastAPI()

setup_logger()

app.add_exception_handler(BaseCustomException, custom_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, system_exception_handler)
app.include_router(api_router, prefix="/api/v1")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """응답 시간 체크용"""
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)

    return response


@app.get("/health", status_code=200)
async def health_check():
    return {"Hello": "World"}


@app.get("/a", status_code=200)
async def error_aa():
    raise Exception("Test Exception")
