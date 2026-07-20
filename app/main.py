from fastapi import FastAPI

from app.database.database import engine, Base
from app.models.medicao import Medicao

from app.routers.medicao_routers import router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TerrariumHub API",
    description="API responsável pelo monitoramento do terrário",
    version="1.0.0"
)

app.include_router(router)

