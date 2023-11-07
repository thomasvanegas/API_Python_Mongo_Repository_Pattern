# Importacion de la clase BaseModel -> Superclase -> pydantic es el serializador y deserializador
from pydantic import BaseModel, Field
# Permite definir un atributo como null
from typing import Optional
from DbContexts.MongoDbContext import PyObjectId

# Definicion del modelo Cargador
class Cargador(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    estado: str = Field(...)
    bus_id: str = Field(...)