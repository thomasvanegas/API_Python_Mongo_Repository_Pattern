# 1. python -m pip install pymongo
# 2. python -m pip install --upgrade pymongo
# 3. MongoDB Container: docker run --name container_name -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=tupw -d mongo
# 4. NOTA: Como sugerencia conectarse al mismo tiempo mediante un cliente GUI al connection string para visualizar cambios (Compass)
# 5. Ejecutar el archivo -> python main.py
# 6. Se puede hacer el connection_string con una URI de MongoDB ATLAS, modificando argumentos como username, password,etc (<argumento>)

from pymongo import MongoClient

# Estableciendo el connection string (Subir docker container y copiar connection string)
connection_string = 'mongodb://mongoadmin:UnaClav3@localhost:27017/?authMechanism=SCRAM-SHA-256'

# Instanciando un cliente de la clase MongoClient y conectandose a dicha instancia
try:
    cliente = MongoClient(connection_string)
except Exception:
    print('Error: ', Exception)

