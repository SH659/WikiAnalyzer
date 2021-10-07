from typing import Optional

from pydantic import BaseModel


class RecentChange(BaseModel):
    id: list[dict]
    event: str
    data: dict


class RecentChangeFilter(BaseModel):
    users: Optional[set[str]]
