from fastapi import FastAPI
from app.core.database import Base,engine
from app.games.router import games
from app.genres.router import genres
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(games)
app.include_router(genres)
