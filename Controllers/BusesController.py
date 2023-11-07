# Importando paquetes
from fastapi import APIRouter
# Importacion del contexto para realizar la conexión
from DbContexts.MongoDbContext import buses_collection
# Importacion de Servicios
from Services.BusService import BusesService, BusService
# Importacion de los Modelos
from Models.Bus import Bus
# Importando el paquete tabulate
from tabulate import tabulate

# Instaciamiento
buses_router = APIRouter()

# --- --- Rutas (HTTP VERBS) para la Entidad/Coleccion Buses --- ---
@buses_router.get('/api/buses')
def find_all_buses():
    return BusesService(buses_collection.find())

# --- --- Obtener un bus dado un _id: ObjectID('')
@buses_router.get('/api/buses/{id}')
def find_bus_by_id():
    return {'placa': 'ABC123'}

# --- --- Crear un nuevo bus
@buses_router.post('/buses')
def insert_new_bus(bus: Bus):
    new_bus = dict(bus)
    
    id = cliente.gestion_buses_cargadores.buses.insert_one(new_bus).inserted_id
    
    table = tabulate(new_bus, headers='keys', tablefmt='fancy_grid')
    print(table)
    
    return f'Bus nuevo creado EXITOSAMENTE con el id {str(id)}'

@buses_router.put('/buses/{id}')
def update_bus():
    return {'placa': 'ABC123'}

@buses_router.delete('/buses/{id}')
def delete_bus():
    return {'placa': 'ABC123'}