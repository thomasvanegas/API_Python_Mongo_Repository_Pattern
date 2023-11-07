# Importacion de Paquetes
from pydantic import BaseModel, Field
from typing import Optional


class Hora(BaseModel):
    hora: int = Field(..., gt=-1, lt=24)
    descripcion: str = Field(...)
    hora_pico: bool = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "hora": 6,
                "descripcion": "6 AM",
                "hora_pico": True,
            }
        }