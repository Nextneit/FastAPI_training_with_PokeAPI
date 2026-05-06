from fastapi import APIRouter
from schemas import PokemonResponse
from services.pokemon_service import pokemon_service

router = APIRouter(prefix="/pokemon", tags=["pokemon"])

@router.get("/{name}", response_model=PokemonResponse)
async def get_pokemon(name: str):
    return await pokemon_service.get_pokemon_data(name)