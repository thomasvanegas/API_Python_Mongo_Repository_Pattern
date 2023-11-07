# 1. python -m pip install pymongo
# 2. python -m pip install --upgrade pymongo
# 3. MongoDB Container: docker run --name container_name -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=tupw -d mongo
# 4. NOTA: Como sugerencia conectarse al mismo tiempo mediante un cliente GUI al connection string para visualizar cambios (Compass)
# 5. Ejecutar el archivo -> python main.py
# 6. Se puede hacer el connection_string con una URI de MongoDB ATLAS, modificando argumentos como username, password,etc (<argumento>)
# 7. Async driver -> pip install motor

# Para Aplicaciones Syncronicas usar MongoCliente
from pymongo import MongoClient
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator

# Para Aplicaciones Async usar Motor
from motor.motor_asyncio import AsyncIOMotorClient

# Estableciendo el connection string (Subir docker container y copiar connection string)
connection_string = 'mongodb://mongoadmin:UnaClav3@localhost:27017/?authMechanism=SCRAM-SHA-256'

client = AsyncIOMotorClient(connection_string)

# ../data/script_creacion_modelo_datos_mongodb.txt
# database = client["gestion_buses_cargadores"] -> Método Alterno
database = client.get_database("gestion_buses_cargadores")

# Colecciones a usar -- buses_collection = database["buses"] -> Método Alterno
buses_collection = database.get_collection("buses")
cargadores_collection = database.get_collection("cargadores")
horas_collection = database.get_collection("horas")

# ObjectId
PyObjectId = Annotated[str, BeforeValidator(str)]