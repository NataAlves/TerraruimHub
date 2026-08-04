from sqlalchemy import Column, Integer, Float, String
from app.database.database import Base

class Medicao(Base):
    __tablename__ = "medicoes"
    id = Column(Integer, primary_key=True, index=True)
    temperatura = Column(Float)
    lampada = Column(String(20))
    data_hora = Column(String(50))

