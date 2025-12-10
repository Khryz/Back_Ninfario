from pydantic import BaseModel
from typing import List

class NinfaCreate(BaseModel):
    nidada: str
    tipo: str
    precio: str
    disponibilidad: str
    imagen:str

class NinfaList(BaseModel):
    ninfas: List[NinfaCreate]
