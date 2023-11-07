# Importando paquetes
from fastapi import APIRouter, HTTPException, Body
from fastapi.responses import Response
from fastapi.encoders import jsonable_encoder
# Importando el paquete tabulate
from tabulate import tabulate
# Importando el ObjectId
from bson.objectid import ObjectId

# Importando las operaciones CRUD del CargadorRepository
from Repositories.HoraRepository import (
    read_all_horas,
    read_hora_by_id,
    update_hora,
    delete_hora,
    create_new_hora
)

# Importacion de los Modelos
from Models.ErrorResponse import ErrorResponse
from Models.Response import Response
from Models.Hora import Hora
from Models.UpdateHora import UpdateHora

# Instaciamiento
router = APIRouter()

@router.post("/", response_description="Crear e Insertar una Nueva Hora a la Base de Datos")
async def insertar_nueva_hora(hora: Hora = Body(...)):
    hora = jsonable_encoder(hora)
    nueva_hora = await create_new_hora(hora)
    return Response(nueva_hora, "Nueva Hora Creada e Insertada a la Base de Datos MongoDB CORRECTAMENTE")

@router.get("/", response_description="Obtener Todas las Horas Almacenados en la BD")
async def get_all_horas():
    horas = await read_all_horas()
    if horas:
        return Response(horas, "Horas Extraidas de la BD MongoDB CORRECTAMENTE")
    return Response(horas, "No Hay Horas Existentes")

@router.get("/{id}", response_description="Obtener una Hora por ID")
async def get_hora_by_id(id):
    hora = await read_hora_by_id(id)
    if hora:
        return Response(hora, f"La Hora con el id {id} fue encontrada CORRECTAMENTE")
    return ErrorResponse("Un Error ha Ocurrido.", 404, "La Hora con ID ingresado No Existe")

@router.put("/{id}")
async def update_hora_by_id(id: str, req: UpdateHora = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    hora_actualizada = await update_hora(id, req)
    if hora_actualizada:
        return Response(
            f"La Hora con ID: {id} ha sido actualizada",
            "Hora Actualizada Correctamente",
        )
    return ErrorResponseModel(
        "Un Error ha Ocurrido :(",
        404,
        "Ha ocurrido un error mientras se actualizaba la Hora Nueva",
    )

@router.delete("/{id}", response_description="Eliminación de una Hora desde la BD")
async def delete_hora_by_id(id: str):
    hora_eliminada = await delete_hora(id)
    if hora_eliminada:
        return Response(
            f"La hora con el ID: {id} Ha Sido ELIMINADA CORRECTAMENTE", "Hora Eliminada Correctamente"
        )
    return ErrorResponseModel(
        "Un Error ha Ocurrido :(",
        404, 
        f"La hora con ID {id} NO EXISTE en la Base de Datos"
    )