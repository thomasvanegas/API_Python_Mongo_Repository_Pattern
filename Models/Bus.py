# Importacion de la clase BaseModel -> Superclase -> pydantic es el serializador y deserializador
from pydantic import BaseModel, Field
from typing import Optional # Permite definir un atributo como nulleable
from DbContexts.MongoDbContext import PyObjectId

# Definicion del modelo -> Todos los modelos heredan de la clase BaseModel
class Bus(BaseModel):
    placa: str = Field(...)
    marca: str = Field(...)
    estado: str = Field(...)
    ult_hora_carga: int = Field(..., gt=-1, lt=24)

    class Config:
        schema_extra = {
            "example": {
                "placa": "ABC123",
                "marca": "BMW",
                "estado": "En Operación",
                "ult_hora_carga": 12
            }
        }