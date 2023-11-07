# Importando paquetes
from fastapi import APIRouter
# Importacion del contexto para realizar la conexión
from DbContexts.MongoDbContext import cargadores_collection
# Importacion de Servicios
from Services.CargadorService import CargadoresServices, CargadorService
# Importacion de los Modelos
from Models.Cargador import Cargador
# Importando el paquete tabulate
from tabulate import tabulate

# Instaciamiento
router = APIRouter()

@router.get("/api/cargadores/", response_model=Cargador)
async def find_all_cargadores():
    pass