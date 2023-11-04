# Importando paquetes
from fastapi import APIRouter
# Importacion del contexto para realizar la conexión
from DbContexts.MongoDbContext import cliente
# Importacion de Servicios
from Services.BusService import BusesService, BusService
# Importacion de los Modelos
from Models.Bus import Bus
# Importando el paquete tabulate
from tabulate import tabulate

# Instaciamiento
router = APIRouter()

# Definicion de ruta raiz
@router.get('/')
def read_root() -> str:
    return 'Hola, Bienvenido a la Implementación de la API como Desarrollo del Parcial N°4 - Gestión de Implementación de Buses y Cargadores'

# --- --- Rutas (HTTP VERBS) para la Entidad/Coleccion Buses --- ---
@router.get('/buses')
def find_all_buses():
    return BusesService(cliente.gestion_buses_cargadores.buses.find())

# --- --- Obtener un bus dado un _id: ObjectID('')
@router.get('/buses/{id}')
def find_bus_by_id():
    return {'placa': 'ABC123'}

# --- --- Crear un nuevo bus
@router.post('/buses')
def insert_new_bus(bus: Bus):
    new_bus = dict(bus)
    
    id = cliente.gestion_buses_cargadores.buses.insert_one(new_bus).inserted_id
    
    table = tabulate(new_bus, headers='keys', tablefmt='fancy_grid')
    print(table)
    
    return f'Bus nuevo creado EXITOSAMENTE con el id {str(id)}'

@router.put('/buses/{id}')
def update_bus():
    return {'placa': 'ABC123'}

@router.delete('/buses/{id}')
def delete_bus():
    return {'placa': 'ABC123'}