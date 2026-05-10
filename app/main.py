from fastapi import FastAPI
from app.core.database import Base,engine
from app.games.router import games
from app.genres.router import genres


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(games)
app.include_router(genres)




