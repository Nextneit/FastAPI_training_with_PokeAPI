from sqlalchemy import Column, Integer, String
from database import Base

class FavoritePokemon(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    pokemon_name = Column(String, unique=True, index=True)
    poke_id = Column(Integer)