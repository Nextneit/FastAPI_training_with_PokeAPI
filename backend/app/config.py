from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Definimos las variables y su tipo (Pydantic las validará)
    pokeapi_base_url: str
    database_url: str

    # Configuración para leer el archivo .env
    model_config = SettingsConfigDict(env_file=".env")

# Instancia global para usar en todo el proyecto
settings = Settings()