# Importacion de la clase BaseModel -> Superclase -> pydantic es el serializador y deserializador
from pydantic import BaseModel, Field
# Permite definir un atributo como null
from typing import Optional, List
from DbContexts.MongoDbContext import PyObjectId
from Models.Bus import Bus

# Definicion de la clase CargadorCollection
class BusCollection (BaseModel):
    """
    
    Contenedor de una lista de instancias del modelo Cargador
    
    """
    cargadores: List[Bus]