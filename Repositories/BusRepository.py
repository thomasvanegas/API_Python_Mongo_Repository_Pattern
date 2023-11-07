# Importación Paquetes
from bson.objectid import ObjectId
from Helpers.BusHelper import bus_helper
from DbContexts.MongoDbContext import buses_collection

# Definición de Operaciones CRUD
async def read_all_buses():
    buses_list = []
    async for bus in buses_collection.find():
        buses_list.append(bus_helper(bus))
    return buses_list

async def read_bus_by_id(id: str) -> dict:
    bus = await buses_collection.find_one({"_id": ObjectId(id)})
    if bus:
        return bus_helper(bus)

async def create_new_bus(bus_data: dict) -> dict:
    bus = await buses_collection.insert_one(bus_data)
    new_bus = await buses_collection.find_one({"_id": bus.inserted_id})
    return bus_helper(new_bus)

async def update_bus(id: str, data: dict):
    # Validando si el cuerpo del request está vacio
    if len(data) < 1:
        return False
    bus = await buses_collection.find_one({"_id": ObjectId(id)})
    if bus:
        bus_actualizado = await buses_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if bus_actualizado:
            return True
        return False

async def delete_bus(id: str):
    bus = await buses_collection.find_one({"_id": ObjectId(id)})
    if bus:
        await buses_collection.delete_one({"_id": ObjectId(id)})
        return True