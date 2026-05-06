from pydantic import BaseModel

class TypeDetail(BaseModel):
    name: str

class PokemonType(BaseModel):
    slot: int
    type: TypeDetail

class PokemonSprites(BaseModel):
    front_default: str | None

class PokemonResponse(BaseModel):
    id: int
    name: str
    height: int
    weight: int
    types: list[PokemonType]
    sprites: PokemonSprites