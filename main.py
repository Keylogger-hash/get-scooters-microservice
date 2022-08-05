from fastapi import FastAPI
from routers import scooters


app = FastAPI()


app.include_router(scooters.router)


