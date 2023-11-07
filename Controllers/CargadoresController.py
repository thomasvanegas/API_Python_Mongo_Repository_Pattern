# Importando paquetes
from fastapi import APIRouter, HTTPException, FastAPI
from fastapi.responses import Response
# Importacion del contexto para realizar la conexión
from DbContexts.MongoDbContext import cargadores_collection
# Importacion de Servicios
# from Services.CargadorService import CargadoresServices, CargadorService
# Importacion de los Modelos
from Models.Cargador import Cargador
from Models.CargadorCollection import CargadorCollection
# Importando el paquete tabulate
from tabulate import tabulate
# Importando el ObjectId
from bson import ObjectId

# Instaciamiento
cargadores_router = APIRouter()

# Obtener todos los cargadores
@cargadores_router.get(
    "/api/cargadores/", 
    response_description="Lista/Colección de Cargadores",
    response_model=CargadorCollection,
    response_model_by_alias=False
)
async def find_all_cargadores():
    cargadores_list = CargadorCollection(cargadores = await cargadores_collection.find().to_list(100))
    return cargadores_list

#Obtener cargador por id
@cargadores_router.get(
    "/api/cargadores/{id}",
    response_description="Obtener un único cargador por Id",
    response_model=Cargador,
    response_model_by_alias=False,
)
async def find_one_cargador(id: str):
    """
    
    Obtener un cargador dado un Id
    
    """
    if (
        cargador := await cargadores_collection.find_one({"_id": ObjectId(id)})
    ) is not None:
        return cargador

    raise HTTPException(status_code=404, detail=f"El cargador con id: {id} no existe")
