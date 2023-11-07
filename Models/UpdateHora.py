# Importación de Paquetes
from pydantic import BaseModel, Field
from typing import Optional

class UpdateHora (BaseModel):
    hora: Optional[int]
    descripcion: Optional[str]
    hora_pico: Optional[bool]