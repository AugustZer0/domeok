from fastapi import FastAPI

from api.v1.api import api_router

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")


@app.get("/health", status_code=200)
async def health_check():
    return {"Hello": "World"}
