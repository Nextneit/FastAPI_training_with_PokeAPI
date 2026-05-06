import pytest
import respx
from httpx import Response
from services.pokemon_service import pokemon_service

@pytest.mark.asyncio  # Necesario para funciones async
async def test_get_pokemon_data_success():
    # 1. Definimos un "falso" Pokémon para el test
    mock_name = "pikachu"
    mock_response_payload = {
        "id": 25,
        "name": "pikachu",
        "height": 4,
        "weight": 60,
        "types": [{"slot": 1, "type": {"name": "electric"}}],
        "sprites": {"front_default": "url_imagen"}
    }

    # 2. Interceptamos la llamada a PokeAPI usando respx
    with respx.mock:
        respx.get(f"https://pokeapi.co/api/v2/pokemon/{mock_name}").mock(
            return_value=Response(200, json=mock_response_payload)
        )

        # 3. Llamamos a nuestro servicio real
        result = await pokemon_service.get_pokemon_data(mock_name)

        # 4. Verificamos que los datos sean correctos
        assert result["name"] == "pikachu"
        assert result["id"] == 25
        assert "types" in result

@pytest.mark.asyncio
async def test_get_pokemon_data_not_found():
    mock_name = "pokemon-falso"

    with respx.mock:
        # Simulamos un 404
        respx.get(f"https://pokeapi.co/api/v2/pokemon/{mock_name}").mock(
            return_value=Response(404)
        )

        # Verificamos que nuestro servicio lanza la excepción correcta
        with pytest.raises(Exception) as excinfo:
            await pokemon_service.get_pokemon_data(mock_name)
        
        assert "404" in str(excinfo.value)