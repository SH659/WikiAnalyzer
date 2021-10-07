import json

import aiohttp

from models.wikimedia.utils import async_stream_tee


def convert_wikimedia_event_bytes_to_json(event: list[bytes]) -> bytes:
    event: bytes
    id_: bytes
    data: bytes
    fields: list[bytes]

    event, id_, data, *fields = event

    res = [b'{']

    # id
    l, m, r = id_.partition(b': ')
    res.extend((b'"', l, b'"', m, r, b','))
    # event
    l, m, r = event.partition(b': ')
    res.extend((b'"', l, b'"', m, b'"', r, b'", '))
    # data
    l, m, r = data.partition(b': ')
    res.extend((b'"', l, b'"', m, r))

    res.append(b'}')
    return b''.join(res).replace(b'\n', b'')


async def aiosseclient(url, last_id=None, **kwargs):
    if 'headers' not in kwargs:
        kwargs['headers'] = {}

    # The SSE spec requires making requests with Cache-Control: nocache
    kwargs['headers']['Cache-Control'] = 'no-cache'

    # The 'Accept' header is not required, but explicit > implicit
    kwargs['headers']['Accept'] = 'text/event-stream'

    if last_id:
        kwargs['headers']['Last-Event-ID'] = last_id

    # Override default timeout of 5 minutes
    timeout = aiohttp.ClientTimeout(total=None, connect=None,
                                    sock_connect=None, sock_read=None)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        response = await session.get(url, **kwargs)
        lines = []
        async for line in response.content:
            if line in {b'\n', b'\r', b'\r\n'}:
                if lines[0] == b':ok\n':
                    lines = []
                    continue

                yield lines
                lines = []
            else:
                lines.append(line)


@async_stream_tee
async def _listen_raw():
    async for event in aiosseclient('https://stream.wikimedia.org/v2/stream/recentchange'):
        yield event


@async_stream_tee
async def listen_raw():
    async for event in _listen_raw():
        yield b''.join(event)


@async_stream_tee
async def listen_json_bytes():
    async for event in _listen_raw():
        yield convert_wikimedia_event_bytes_to_json(event) + b'\n'


@async_stream_tee
async def listen_json():
    async for event in listen_json_bytes():
        yield json.loads(event)
