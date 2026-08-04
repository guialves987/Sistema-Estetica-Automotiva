"""
Ponto de entrada da aplicação.

Responsável por:
- Criar a instância do FastAPI.
- Configurar informações da API.
- Registrar as rotas do sistema.
"""

from fastapi import FastAPI
from app.core.config import settings

from app.routes.cliente_routes import router as cliente_router
from app.routes.veiculo_routes import router as veiculo_router

# Instância principal da aplicação
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

# Registro das rotas da aplicação
app.include_router(cliente_router)
app.include_router(veiculo_router)

@app.get("/")
def root():
    """
    Endpoint inicial utilizado para verificar
    se a API está em funcionamento.
    """
    return {
        "message": "API do Sistema de Estética Automotiva funcionando"
    }