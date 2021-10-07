import json

import aiohttp

import schemas


async def get_by_user(data: schemas.ContributionsRequest) -> dict:
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "usercontribs",
        "ucuser": data.user
    }
    if data.ucstart is not None:
        params['ucstart'] = data.ucstart.isoformat() + "Z"

    if data.ucend is not None:
        params['ucend'] = data.ucend.isoformat() + "Z"

    async with aiohttp.ClientSession() as session:
        response = await session.get(url, params=params)
        res = json.loads(await response.read())
    return {'usercontribs': res['query']['usercontribs']}
