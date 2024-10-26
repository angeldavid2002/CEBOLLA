from fastapi import FastAPI
from app.interface.api import router

app = FastAPI()

# Incluir el router
app.include_router(router)
