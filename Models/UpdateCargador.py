from pydantic import BaseModel, Field
from typing import Optional
from DbContexts.MongoDbContext import PyObjectId

class UpdateCargador(BaseModel):
    estado: Optional[str]
    bus_id: Optional[str]