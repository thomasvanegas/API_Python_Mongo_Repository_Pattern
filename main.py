# Importando uvicorn
import uvicorn

# Importando el framework FastAPI
from fastapi import FastAPI
from typing import Union

# Importando Controllers
from Controllers.BusesController import router

# Instanciamiento
app = FastAPI()

app.include_router(router)