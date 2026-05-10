from pydantic import BaseModel, ConfigDict
from datetime import datetime


class GenreNested(BaseModel):
    id : int
    name: str
    model_config = ConfigDict(from_attributes=True)

class GameCreate(BaseModel):
    title: str
    release_year: int
    platform: str
    genre_id : int


class GameResponse(BaseModel):
    id: int
    title: str
    release_year: int
    platform: str
    genre: GenreNested
    created_at : datetime
    model_config = ConfigDict(from_attributes=True)


