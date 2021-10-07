import itertools
import logging
from datetime import datetime

from fastapi import APIRouter

import schemas
from models import wikimedia

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post('/', response_model=schemas.ContributionsResponse)
async def get_user_contributions(data: schemas.ContributionsRequest):
    return {'user_contributions': await wikimedia.contributions.get_by_user(data.user, data.ucstart, data.ucend)}


@router.post('/stats_over_time', response_model=schemas.ContributionsStatsOverTimeResponse)
async def get_stats_over_time(data: schemas.ContributionsStatsOverTimeRequest):
    contributions = await wikimedia.contributions.get_by_user(data.user, data.ucstart, data.ucend)

    def group_contribution(contrib):
        dt = datetime.fromisoformat(contrib['timestamp'][:-1])
        return dt + (datetime.min - dt) % data.interval

    contributions_over_time = []
    for interval_end, contributions in itertools.groupby(contributions, key=group_contribution):
        c = list(contributions)
        contributions_over_time.append({
            "interval_start": interval_end - data.interval,
            "interval_end": interval_end,
            "contributions_count": len(c),
            "contributions": c
        })
    return {"contributions_over_time": contributions_over_time}
