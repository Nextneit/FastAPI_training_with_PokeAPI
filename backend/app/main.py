from fastapi import FastAPI
from router import pokemon
import httpx

app = FastAPI()

app.include_router(pokemon.router)

async def get_http_client():
    async with httpx.AsyncClient() as client:
        yield client

@app.get("/health")
def	healthCheck():
    return ({"status": "running"})