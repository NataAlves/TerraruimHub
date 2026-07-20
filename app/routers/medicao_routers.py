from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.medicao_service import (listar_medicoes,adicionar_medicoes)
from app.schemas.medicao import Medicao

from app.database.database import get_db

################## FIM dos IMPORTS ############

router = APIRouter(
    prefix="/medicoes",
    tags=["Medições"]
)

@router.get('/status')    
def home():
    return{"mensagem":"API TerrariumHub Online"}

@router.get('/')
def buscar_medicoes(db: Session = Depends(get_db)):
    return listar_medicoes(db)

@router.post('/')
def recebe_medicao (medicao:Medicao,db:Session = Depends(get_db)):
    adicionar_medicoes(db,medicao)

    return{
        "resposta":"add com sucesso"
    }
 