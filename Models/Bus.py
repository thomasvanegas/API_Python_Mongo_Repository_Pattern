# Importacion de la clase BaseModel -> Superclase
from pydantic import BaseModel
from typing import Optional # Permite definir un atributo como nulleable

# Definicion del modelo -> Todos los modelos heredan de la clase BaseModel
class Bus(BaseModel):
    placa: str
    marca: str
    estado: str
    ult_hora_carga: int