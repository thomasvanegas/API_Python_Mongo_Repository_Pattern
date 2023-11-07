# Importando paquetes
from fastapi import APIRouter, HTTPException, Body
from fastapi.responses import Response
from fastapi.encoders import jsonable_encoder
# Importando el paquete tabulate
from tabulate import tabulate
# Importando el ObjectId
from bson.objectid import ObjectId

# Importando las operaciones CRUD del CargadorRepository
from Repositories.CargadorRepository import (
    read_all_cargadores,
    read_cargador_by_id,
    update_cargador,
    delete_cargador,
    create_new_cargador
)

# Importacion de los Modelos
from Models.ErrorResponse import ErrorResponse
from Models.Response import Response
from Models.Cargador import Cargador
from Models.UpdateCargador import UpdateCargador

# Instaciamiento
router = APIRouter()

@router.post("/", response_description="Crear e Insertar un Nuevo Cargador a la Base de Datos")
async def insertar_nuevo_cargador(cargador: Cargador = Body(...)):
    cargador = jsonable_encoder(cargador)
    nuevo_cargador = await create_new_cargador(cargador)
    return Response(nuevo_cargador, "Cargador Creado e Insertado a la BD CORRECTAMENTE")

@router.get("/", response_description="Obtener Todos los Cargadores")
async def get_all_cargadores():
    cargadores = await read_all_cargadores()
    if cargadores:
        return Response(cargadores, "Cargadores Extraidos de la BD CORRECTAMENTE")
    return Response(cargadores, "No Hay Cargadores")

@router.get("/{id}", response_description="Obtener un Cargador por ID")
async def get_cargador_by_id(id):
    cargador = await read_cargador_by_id(id)
    if cargador:
        return Response(cargador, f"Cargador con el id {id} fue encontrado CORRECTAMENTE")
    return ErrorResponse("Un Error ha Ocurrido.", 404, "El cargador con ID ingresado No Existe")

@router.put("/{id}")
async def update_cargador_by_id(id: str, req: UpdateCargador = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    cargador_actualizado = await update_cargador(id, req)
    if cargador_actualizado:
        return Response(
            f"El Cargadpr con ID: {id} ha sido actualizado",
            "Cargador Actualizado Correctamente",
        )
    return ErrorResponseModel(
        "Un Error ha Ocurrido :(",
        404,
        "Ha ocurrido un erro mientras se actualizaba el cargador",
    )

@router.delete("/{id}", response_description="Eliminación de un Cargador desde la BD")
async def delete_cargador_by_id(id: str):
    cargador_eliminado = await delete_cargador(id)
    if cargador_eliminado:
        return Response(
            f"El Cargador con el ID: {id} Ha Sido ELIMINADO CORRECTAMENTE", "Cargador Eliminado Correctamente"
        )
    return ErrorResponseModel(
        "Un Error ha Ocurrido :(",
        404, 
        f"El cargador con ID {id} NO EXISTE en la Base de Datos"
    )