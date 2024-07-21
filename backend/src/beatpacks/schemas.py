from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

from src.beatpacks.models import Beatpack
from src.beats.schemas import SBeat

class SBeatpackBase(BaseModel):
    title: str
    description: str
    owner_id: int
    beats: List[SBeat] = Field(...)
    
class SBeatPackCreate(SBeatpackBase):
    pass

class SBeatPack(SBeatpackBase):
    id: int
    liked: bool
    is_available: bool
    created_at: datetime

    class Config:
        orm_mode = True

class SBeatpackEditResponse(BaseModel):
    response: str = "Beat pack edited"


class SBeatpackDeleteResponse(BaseModel):
    response: str = "Beat pack deleted"

class SBeatpackResponse(BaseModel):
    id: int
    description: str
    is_available: bool
    title: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_db_model(cls, beatpack: Beatpack) -> 'SBeatpackResponse':
        return cls(
            id=beatpack.id,
            description=beatpack.description,
            is_available=beatpack.is_available,
            title=beatpack.title,
            created_at=beatpack.created_at,
            updated_at=beatpack.updated_at
        )
