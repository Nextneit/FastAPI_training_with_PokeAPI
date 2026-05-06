from fastapi import HTTPException
from app.config import settings
import httpx

class PokemonService:
	def __init__(self):
		self.baseUrl = settings.pokeapi_base_url
  
	async def get_pokemon_data(self, name : str):
		async with httpx.AsyncClient() as client:
			try:
				response = await client.get(f"{self.baseUrl}{name.lower()}")
                
				if response.status_code == 404:
					raise HTTPException(status_code=404, detail="Pokémon no encontrado en el laboratorio")
                
				response.raise_for_status()
				return response.json()
                
			except httpx.RequestError as exc:
				raise HTTPException(status_code=503, detail=f"Error de conexión con PokeAPI: {exc}")

pokemon_service = PokemonService()