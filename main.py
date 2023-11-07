# Importando uvicorn
import uvicorn

# Importando el framework FastAPI
from fastapi import FastAPI
from typing import Union

# Importando Controllers
from Controllers.CargadoresController import cargadores_router
from Controllers.BusesController import buses_router

# Instanciamiento
app = FastAPI()

app.include_router(cargadores_router)
app.include_router(buses_router)