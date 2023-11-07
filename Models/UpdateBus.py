# Importación de Paquetes
from pydantic import BaseModel, Field
from typing import Optional

class UpdateBus (BaseModel):
    placa: Optional[str]
    marca: Optional[str]
    estado: Optional[str]
    ult_hora_carga: Optional[int]