# Importando uvicorn
import uvicorn

# Importando el framework FastAPI
from fastapi import FastAPI
from typing import Union

# Importando Controllers
from Controllers.CargadoresController import router as CargadorRouter
from Controllers.BusesController import router as BusRouter
from Controllers.HorasController import router as HoraRouter

# Instanciamiento
app = FastAPI()

app.include_router(CargadorRouter, tags=["Cargador"], prefix="/api/cargadores")
app.include_router(BusRouter, tags=["Bus"], prefix="/api/buses")
app.include_router(HoraRouter, tags=["Hora"], prefix="/api/horas")

# --- --- Definición de la ruta inicial --- ---
@app.get("/", tags=["Root"])
async def read_root() -> list:
    response_list = [
        {"Mensaje:": "Hola, Bienvenido a la Implementación de la API como Desarrollo del Parcial N°4 - Gestión de Implementación de Buses y Cargadores"},
        {"IMPORTANTE:": "Para empezar a hacer uso de la API recuerda usar las rutas iniciadas en http://localhost:8000/api"},
        {"RECUERDA": "Si deseas conocer qué rutas están desarrolladas en la API dirigete a: http://localhost:8000/docs/"}
    ]
    return response_list