import logging

from fastapi import APIRouter

import schemas
from models import wikimedia

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post('/', response_model=schemas.ContributionsResponse)
async def get_user_contributions(data: schemas.ContributionsRequest):
    return await wikimedia.contributions.get_by_user(data)
