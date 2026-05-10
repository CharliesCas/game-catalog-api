from sqlalchemy.orm import Session
from app.games.models import Game

def get_game(db: Session,id: int):
    return db.query(Game).filter(Game.id == id).first()

def get_name_game(db: Session, title: str):
    return db.query(Game).filter(Game.title == title).first()

def get_all_games(db: Session):
    return db.query(Game).all()

def get_games_by_genre(db: Session, genre_id :int):
    return db.query(Game).filter(Game.genre_id == genre_id).all()

def create_game(db: Session, title: str, release_year: int, platform: str, genre_id: int):
    new_game = Game(title=title,release_year=release_year,platform=platform,genre_id=genre_id)
    db.add(new_game)
    db.commit()
    db.refresh(new_game)
    return new_game

def update_game(db: Session, game: Game):
    db.commit()
    db.refresh(game)
    return game
    

def delete_game(db: Session, game: Game):
    db.delete(game)
    db.commit()
    return True