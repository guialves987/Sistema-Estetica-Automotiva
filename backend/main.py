from fastapi import FastAPI
from app.core.config import settings

from app.routes.cliente_routes import router as cliente_router
from app.routes.veiculo_routes import router as veiculo_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

app.include_router(cliente_router)

@app.get("/")
def root():
    return {
        "message": "API do Sistema de Estética Automotiva funcionando"
    }

app.include_router(veiculo_router)