# Importación Paquetes
from bson.objectid import ObjectId
from Helpers.CargadorHelper import cargador_helper
from DbContexts.MongoDbContext import cargadores_collection, buses_collection

# Definición de Operaciones CRUD
async def read_all_cargadores():
    cargadores_list = []
    async for cargador in cargadores_collection.find():
        cargadores_list.append(cargador_helper(cargador))
    return cargadores_list

async def read_cargador_by_id(id: str) -> dict:
    cargador = await cargadores_collection.find_one({"_id": ObjectId(id)})
    if cargador:
        return cargador_helper(cargador)

async def create_new_cargador(cargador_data: dict) -> dict:
    cargador = await cargadores_collection.insert_one(cargador_data)
    nuevo_cargador = await cargadores_collection.find_one({"_id": cargador.inserted_id})
    return cargador_helper(nuevo_cargador)

async def update_cargador(id: str, data: dict):
    # Validando si el cuerpo del request está vacio
    if len(data) < 1:
        return False
    cargador = await cargadores_collection.find_one({"_id": ObjectId(id)})
    if cargador:
        cargador_actualizado = await cargadores_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if cargador_actualizado:
            return True
        return False

async def delete_cargador(id: str):
    cargador = await cargadores_collection.find_one({"_id": ObjectId(id)})
    if cargador:
        await cargadores_collection.delete_one({"_id": ObjectId(id)})
        return True
