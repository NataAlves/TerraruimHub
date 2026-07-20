from pydantic import BaseModel

class Medicao(BaseModel):
    temperatura: float
    lampada: str
    data_hora: str

