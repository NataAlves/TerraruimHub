from sqlalchemy import Column, Integer, Float, String
from app.database.database import Base, engine

class Medicao(Base):
    __tablename__ = "medicoes"
    id = Column(Integer, primary_key=True, index=True)
    temperatura = Column(Float)
    lampada = Column(String)
    data_hora = Column(String)

