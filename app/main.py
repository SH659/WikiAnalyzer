from fastapi import FastAPI

from api.api_v1.api import api_router
from core.settings import settings

app = FastAPI(
    title='WikiAnalyzer',
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/",
    redoc_url="/docs",
)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/health", include_in_schema=False)
async def health():
    return {"message": "ok"}
