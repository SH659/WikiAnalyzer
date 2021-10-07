from fastapi import APIRouter

from .endpoints import recent_changes, contributions

api_router = APIRouter()
api_router.include_router(recent_changes.router, prefix='/recent_changes', tags=['recent_changes'])
api_router.include_router(contributions.router, prefix='/contributions', tags=['contributions'])
