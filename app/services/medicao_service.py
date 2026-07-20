from sqlalchemy.orm import Session
from app.models.medicao import Medicao

def listar_medicoes(db: Session):
    return db.query(Medicao).all()


def adicionar_medicoes(db: Session,medicao):
    nova_medicao = Medicao(
        temperatura = medicao.temperatura,
        lampada = medicao.lampada,
        data_hora = medicao.data_hora
    )
    
    db.add(nova_medicao)
    db.commit()
    db.refresh(nova_medicao)
    return nova_medicao
