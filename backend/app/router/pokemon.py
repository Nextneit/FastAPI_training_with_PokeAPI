from fastapi import APIRouter, Depends
from schemas import PokemonResponse
from services.pokemon_service import pokemon_service
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter(prefix="/pokemon", tags=["pokemon"])

@router.get("/favorites")
async def get_all_favorites(db: Session = Depends(get_db)):
    # Esto equivale a un "SELECT * FROM favorites"
    favs = db.query(models.FavoritePokemon).all()
    return favs

@router.get("/{name}", response_model=PokemonResponse)
async def get_pokemon(name: str):
    return await pokemon_service.get_pokemon_data(name)

@router.post("/favorite/{name}/{poke_id}")
async def add_favorite(name: str, poke_id: int, db: Session = Depends(get_db)):
    existing = db.query(models.FavoritePokemon).filter(models.FavoritePokemon.pokemon_name == name).first()
    if existing:
        return {"message": f"{name} ya está en tus favoritos"}

    new_fav = models.FavoritePokemon(pokemon_name=name.lower(), poke_id=poke_id)
    db.add(new_fav)
    db.commit()
    db.refresh(new_fav)
    
    return {"message": f"{name} añadido a favoritos", "db_id": new_fav.id}