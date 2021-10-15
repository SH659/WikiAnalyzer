import asyncio
import logging
from typing import TypeVar, AsyncIterable, Optional, Callable

T = TypeVar('T')


class _AtFunctionExit:
    def __init__(self, func):
        self.func = func

    def __del__(self):
        self.func()


def at_function_exit(func):
    return _AtFunctionExit(func)


def async_stream_tee(aiter_: Callable[[], AsyncIterable[T]]) -> Callable[[], AsyncIterable[T]]:
    value_changed_event: Optional[asyncio.Event] = None
    value: T = None
    subscribers_count: int = 0
    listen_task: Optional[asyncio.Task] = None

    async def _listen() -> None:
        nonlocal value_changed_event, value
        async for value in aiter_():
            value_changed_event.set()
            value_changed_event.clear()

    def _decrease_listeners_count():
        nonlocal subscribers_count, listen_task
        subscribers_count -= 1
        if subscribers_count == 0:
            listen_task.cancel()
            listen_task = None

    async def observe() -> AsyncIterable[T]:
        nonlocal subscribers_count, listen_task, value_changed_event
        if value_changed_event is None:
            value_changed_event = asyncio.Event()
        subscribers_count += 1
        at_func_exit = at_function_exit(_decrease_listeners_count)

        if listen_task is None:
            listen_task = asyncio.create_task(_listen())

        while True:
            await value_changed_event.wait()
            yield value

    return observe
