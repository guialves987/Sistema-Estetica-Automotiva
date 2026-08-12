"""
Rotas relacionadas aos veículos.

Responsáveis por receber as requisições HTTP
e encaminhá-las para a camada de serviços.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.veiculo import(
    VeiculoCreate,
    VeiculoResponse,
    VeiculoUpdate
)   

from app.services.veiculo_service import (
    criar_veiculo,
    listar_veiculos,
    buscar_veiculo_por_id,
    atualizar_veiculo
)

# Agrupa todos os endpoints relacionados a veículos
router = APIRouter(
    prefix="/veiculos",
    tags=["Veículos"]
)

@router.post(
    "/",
    response_model=VeiculoResponse
)
def criar_veiculo_endpoint(
    veiculo: VeiculoCreate,
    db: Session = Depends(get_db)
):
    return criar_veiculo(
        db=db,
        veiculo=veiculo
    )

@router.get(
    "/",
    response_model=list[VeiculoResponse]
)
def listar_veiculos_endpoint(
    db: Session = Depends(get_db)
):
    return listar_veiculos(db)

@router.get(
    "/{veiculo_id}",
    response_model=VeiculoResponse
)
def buscar_veiculo(
    veiculo_id: int,
    db: Session = Depends(get_db)
):
    return buscar_veiculo_por_id(
        db,
        veiculo_id
    )

@router.put(
    "/{veiculo_id}",
    response_model=VeiculoResponse
)
def atualizar_veiculo_endpoint(
    veiculo_id: int,
    dados: VeiculoUpdate,
    db: Session = Depends(get_db)
):
    return atualizar_veiculo(
        db,
        veiculo_id,
        dados
    )