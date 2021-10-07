import json
import logging

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

import schemas
from models import wikimedia

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get('/raw', response_model=schemas.RecentChange)
async def recent_changes():
    return StreamingResponse(wikimedia.recent_changes.listen_raw())


@router.post('/json')
async def recent_changes_by_users(data: schemas.RecentChangeFilter):
    if data.users is None:
        return StreamingResponse(wikimedia.recent_changes.listen_json_bytes())

    async def filtered_stream():
        async for event in wikimedia.recent_changes.listen_json():
            if data.users is not None and event['data'].get('user') in data.users:
                yield json.dumps(event).encode() + b'\n'

    return StreamingResponse(filtered_stream())
