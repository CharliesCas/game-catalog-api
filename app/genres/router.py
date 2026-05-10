from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.genres.schemas import GenreCreate, GenreResponse
from app.genres.services import create_genre_service,get_all_genres_service, get_genre_service, get_name_genre_service


genres = APIRouter()

@genres.get("/genres",response_model=list[GenreResponse])
async def get_genres(db: Session = Depends(get_db)):
    return get_all_genres_service(db)

@genres.post("/genres",response_model=GenreResponse)
async def create_genre(new_genre: GenreCreate, db: Session = Depends(get_db)):
    genre = create_genre_service(db,new_genre.name)
    if genre is True:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Genero ya creado")
    return genre

