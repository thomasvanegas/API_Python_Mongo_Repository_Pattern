# Importando paquetes
from fastapi import APIRouter, HTTPException, Body
from fastapi.responses import Response
from fastapi.encoders import jsonable_encoder
# Importando el paquete tabulate
from tabulate import tabulate
# Importando el ObjectId
from bson.objectid import ObjectId

# Importando las operaciones CRUD del CargadorRepository
from Repositories.BusRepository import (
    read_all_buses,
    read_bus_by_id,
    update_bus,
    delete_bus,
    create_new_bus
)

# Importacion de los Modelos
from Models.ErrorResponse import ErrorResponse
from Models.Response import Response
from Models.Bus import Bus
from Models.UpdateBus import UpdateBus

# Instaciamiento
router = APIRouter()

@router.post("/", response_description="Crear e Insertar un Nuevo Bus a la Base de Datos")
async def insertar_nuevo_bus(bus: Bus = Body(...)):
    bus = jsonable_encoder(bus)
    nuevo_bus = await create_new_bus(bus)
    return Response(nuevo_bus, "Nuevo Bus Creado e Insertado a la Base de Datos MongoDB CORRECTAMENTE")

@router.get("/", response_description="Obtener Todos los Buses Almacenados en la BD")
async def get_all_buses():
    buses = await read_all_buses()
    if buses:
        return Response(buses, "Buses Extraidos de la BD MongoDB CORRECTAMENTE")
    return Response(buses, "No Hay Buses Existentes")

@router.get("/{id}", response_description="Obtener un Bus por ID")
async def get_bus_by_id(id):
    bus = await read_bus_by_id(id)
    if bus:
        return Response(bus, f"El Bus con el id {id} fue encontrado CORRECTAMENTE")
    return ErrorResponse("Un Error ha Ocurrido.", 404, "El bus con ID ingresado No Existe")

@router.put("/{id}")
async def update_bus_by_id(id: str, req: UpdateBus = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    bus_actualizado = await update_bus(id, req)
    if bus_actualizado:
        return Response(
            f"El Bus con ID: {id} ha sido actualizado",
            "Bus Actualizado Correctamente",
        )
    return ErrorResponseModel(
        "Un Error ha Ocurrido :(",
        404,
        "Ha ocurrido un error mientras se actualizaba el Bus Nuevo",
    )

@router.delete("/{id}", response_description="Eliminación de un Bus desde la BD")
async def delete_bus_by_id(id: str):
    bus_eliminado = await delete_bus(id)
    if bus_eliminado:
        return Response(
            f"El Bus con el ID: {id} Ha Sido ELIMINADO CORRECTAMENTE", "Cargador Eliminado Correctamente"
        )
    return ErrorResponseModel(
        "Un Error ha Ocurrido :(",
        404, 
        f"El Bus con ID {id} NO EXISTE en la Base de Datos"
    )