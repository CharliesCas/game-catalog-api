from sqlalchemy.orm import Session
from app.genres.repository import get_genre, get_name_genre, get_all_genres, create_genre

def get_genre_service(db: Session, id: int):
    genre = get_genre(db,id)
    if genre is None:
        return None
    return genre

def get_all_genres_service(db: Session):
    return get_all_genres(db)

def get_name_genre_service(db: Session, name: str):
    genre = get_name_genre(db,name)
    if genre is None:
        return None
    return genre

def create_genre_service(db: Session, name: str):
    is_exists = get_name_genre(db,name)
    if is_exists is not None:
        return True
    return create_genre(db,name)
    