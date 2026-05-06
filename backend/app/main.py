from fastapi import FastAPI
from router import pokemon
from database import engine
import models
import httpx
import time
from sqlalchemy.exc import OperationalError

def create_tables():
    retries = 5
    while retries > 0:
        try:
            models.Base.metadata.create_all(bind=engine)
            break
        except OperationalError:
            retries -= 1
            print(f"Esperando a la DB... ({retries} intentos restantes)")
            time.sleep(3)

create_tables()

app = FastAPI()

app.include_router(pokemon.router)

async def get_http_client():
    async with httpx.AsyncClient() as client:
        yield client

@app.get("/health")
def	healthCheck():
    return ({"status": "running"})