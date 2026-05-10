from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.games.schemas import GameCreate, GameResponse
from app.games.services import create_game_service, get_all_games_services, get_game_service, get_name_game_service, delete_game_service, update_game_service, get_games_by_genre_service
from app.genres.services import get_genre_service
from typing import Optional

games = APIRouter()

@games.get("/games", response_model=list[GameResponse])
async def get_games(genre_id: Optional[int] = None, db: Session = Depends(get_db)):
    if genre_id is not None:
        if get_genre_service(db,genre_id) is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Categoria no existente")
        return get_games_by_genre_service(db,genre_id)
    else:
        return get_all_games_services(db)

@games.get("/games/{id}",response_model=GameResponse)
async def get_game(id: int, db : Session = Depends(get_db)):
    game = get_game_service(db,id)
    if game is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Juego no encontrado")
    return game


@games.post("/games",response_model=GameResponse)
async def create_game(new_game: GameCreate, db: Session = Depends(get_db)):
    if get_genre_service(db,new_game.genre_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Genero al agregar el juego no existente")
    if get_name_game_service(db,new_game.title) is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Juego ya agregado al catalogo")
    
    return create_game_service(db,new_game.title,new_game.release_year, new_game.platform,new_game.genre_id)


@games.put("/games/{id}", response_model=GameResponse)
async def update_game(id: int,updated_game: GameCreate, db: Session = Depends(get_db)):
    if get_game_service(db,id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Juego a actualizar no existente")
    return update_game_service(db,id,updated_game.title,updated_game.release_year,updated_game.platform,updated_game.genre_id)

@games.delete("/games/{id}")
async def delete_game(id: int, db: Session = Depends(get_db)):
    if get_game_service(db,id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Juego a eliminar no existente")
    return delete_game_service(db,id)