from typing import Optional

from pydantic import Field, BaseModel
from pydantic.schema import datetime


class ContributionsRequest(BaseModel):
    user: str = Field()
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


class ContributionsResponse(BaseModel):
    usercontribs: list[dict]
