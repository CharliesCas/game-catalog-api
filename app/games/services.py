from sqlalchemy.orm import Session
from app.games.repository import get_game, get_all_games, get_name_game, create_game, delete_game, update_game, get_games_by_genre

def get_game_service(db: Session, id: int):
    game = get_game(db,id)
    if game is None:
        return None
    return game

def get_name_game_service(db: Session, title: str):
    game = get_name_game(db,title)
    if game is None:
        return None
    return game

def get_games_by_genre_service(db: Session, genre_id: int):
    return get_games_by_genre(db,genre_id)

def get_all_games_services(db: Session):
    return get_all_games(db)

def create_game_service(db: Session, title: str, release_year: int, platform: str, genre_id: int):
    is_exists = get_name_game(db,title)
    if is_exists is not None:
        return True 
    return create_game(db,title,release_year,platform,genre_id)

def update_game_service(db: Session, id: int, title: str, release_year: int, platform: str, genre_id: int):
    game = get_game(db,id)
    if game is None:
        return False      
    
    game.title = title
    game.release_year = release_year
    game.platform = platform
    game.genre_id = genre_id
    return update_game(db,game)
    
      
    
def delete_game_service(db: Session, id: int):
    game = get_game(db,id)
    if game is None:
        return None
    return delete_game(db,game)


