import json
from datetime import datetime

import aiohttp


async def get_by_user(user: str, ucstart: datetime = None, ucend: datetime = None) -> dict:
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "usercontribs",
        "ucuser": user
    }
    if ucstart is not None:
        params['ucstart'] = ucstart.isoformat() + "Z"

    if ucend is not None:
        params['ucend'] = ucend.isoformat() + "Z"

    async with aiohttp.ClientSession() as session:
        response = await session.get(url, params=params)
        res = json.loads(await response.read())
    return res['query']['usercontribs']
