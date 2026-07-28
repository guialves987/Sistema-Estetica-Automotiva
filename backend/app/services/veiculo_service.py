from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models.cliente import Cliente
from app.models.veiculo import Veiculo

from app.schemas.veiculo import(
    VeiculoCreate
)

def obter_veiculo_ou_404(
        db: Session,
        veiculo_id: int
) -> Veiculo:
    veiculo = (
        db.query(Veiculo)
        .filter(Veiculo.id == veiculo_id)
        .first()
    )

    if not veiculo:
        raise HTTPException(
            status_code=404,
            detail="Veículo não encontrado"
        )

    return veiculo

def criar_veiculo(
        db: Session,
        veiculo: VeiculoCreate
) -> Veiculo:

    cliente = (
        db.query(Cliente)
        .filter(
            Cliente.id == veiculo.cliente_id
        )
        .first()
    )

    if not cliente:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )

    placa_existente = (
        db.query(Veiculo)
        .filter(
            Veiculo.placa == veiculo.placa
        )
        .first()
    )

    if placa_existente:
        raise HTTPException(
            status_code=409,
            detail="Já existe um veículo cadastrado com essa placa"
        )

    novo_veiculo = Veiculo(
        cliente_id=veiculo.cliente_id,
        placa=veiculo.placa,
        marca=veiculo.marca,
        modelo=veiculo.modelo,
        ano=veiculo.ano,
        cor=veiculo.cor,
        observacoes=veiculo.observacoes
    )

    db.add(novo_veiculo)
    db.commit()
    db.refresh(novo_veiculo)

    return novo_veiculo