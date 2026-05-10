from sqlalchemy.orm import Session
from app.genres.models import Genre

def get_genre(db: Session, id: int):
    return db.query(Genre).filter(Genre.id == id).first()

def get_all_genres(db: Session):
    return db.query(Genre).all()

def get_name_genre(db: Session, name: str):
    return db.query(Genre).filter(Genre.name == name).first()

def create_genre(db: Session, name: str):
    new_genre = Genre(name=name)
    db.add(new_genre)
    db.commit()
    db.refresh(new_genre)
    return new_genre