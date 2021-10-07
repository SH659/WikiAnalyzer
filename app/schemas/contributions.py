from typing import Optional

from pydantic import BaseModel, Field
from pydantic.schema import datetime, timedelta


class ContributionsRequest(BaseModel):
    user: str
    ucstart: Optional[datetime]
    ucend: Optional[datetime]

    class Config:
        schema_extra = {
            "example": {
                "user": "Jimbo Wales",
                "ucstart": "2021-01-13T00:00:00",
                "ucend": "2021-01-12T00:00:00"
            }
        }


class ContributionsStatsOverTimeRequest(BaseModel):
    user: str
    ucstart: Optional[datetime]
    ucend: Optional[datetime]
    interval: Optional[timedelta] = Field(default=timedelta(days=1), description="interval in seconds")

    class Config:
        schema_extra = {
            "example": {
                "user": "Jimbo Wales",
                "ucstart": "2021-01-15T00:00:00",
                "ucend": "2021-01-01T00:00:00",
                "interval": timedelta(days=1)
            }
        }


class ContributionsResponse(BaseModel):
    user_contributions: list[dict]


class ContributionsStatsOverTimeResponseItem(BaseModel):
    interval_start: datetime
    interval_end: datetime
    contributions_count: int
    contributions: list


class ContributionsStatsOverTimeResponse(BaseModel):
    contributions_over_time: list[dict]
