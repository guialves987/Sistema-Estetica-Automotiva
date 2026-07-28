from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.veiculo import(
    VeiculoCreate,
    VeiculoResponse
)

from app.services.veiculo_service import (
    criar_veiculo
)

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