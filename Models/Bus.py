# Importacion de la clase BaseModel -> Superclase -> pydantic es el serializador y deserializador
from pydantic import BaseModel, Field
from typing import Optional # Permite definir un atributo como nulleable
from DbContexts.MongoDbContext import PyObjectId

# Definicion del modelo -> Todos los modelos heredan de la clase BaseModel
class Bus(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    placa: str
    marca: str
    estado: str
    ult_hora_carga: int = Field(..., gt=-1, lt=24)