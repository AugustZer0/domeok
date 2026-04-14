from fastapi import FastAPI
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

app = FastAPI()

app.add_exception_handler(BaseCustomException, custom_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, system_exception_handler)
app.include_router(api_router, prefix="/api/v1")


@app.get("/health", status_code=200)
async def health_check():
    return {"Hello": "World"}


@app.get("/a", status_code=200)
async def error_aa():
    return Exception
