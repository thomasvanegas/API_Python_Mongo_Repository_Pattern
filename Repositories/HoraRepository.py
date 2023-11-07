# Importación Paquetes
from bson.objectid import ObjectId
from Helpers.HoraHelper import hora_helper
from DbContexts.MongoDbContext import horas_collection

# Definición de Operaciones CRUD
async def read_all_horas():
    horas_list = []
    async for hora in horas_collection.find():
        horas_list.append(hora_helper(hora))
    return horas_list

async def read_hora_by_id(id: str) -> dict:
    hora = await horas_collection.find_one({"_id": ObjectId(id)})
    if hora:
        return hora_helper(hora)

async def create_new_hora(hora_data: dict) -> dict:
    hora = await horas_collection.insert_one(hora_data)
    new_hora = await horas_collection.find_one({"_id": hora.inserted_id})
    return hora_helper(new_hora)

async def update_hora(id: str, data: dict):
    # Validando si el cuerpo del request está vacio
    if len(data) < 1:
        return False
    hora = await horas_collection.find_one({"_id": ObjectId(id)})
    if hora:
        hora_actualizada = await horas_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if hora_actualizada:
            return True
        return False

async def delete_hora(id: str):
    hora = await horas_collection.find_one({"_id": ObjectId(id)})
    if hora:
        await horas_collection.delete_one({"_id": ObjectId(id)})
        return True