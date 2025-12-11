from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Ninfa(Base):
    __tablename__ = "ninfas"

    id = Column(Integer, primary_key=True, index=True)
    nidada = Column(String(255), nullable=False)
    tipo = Column(String(255), nullable=False)
    precio = Column(String(255), nullable=False)
    disponibilidad = Column(String(255), nullable=False)
    imagen = Column(String(255), nullable=False)
