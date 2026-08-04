"""
Serviços responsáveis pelas regras de negócio relacionadas
a veículos.

Esta camada concentra operações de criação,
consulta e validação dos veículos cadastrados.
"""

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
    """
    Busca um veículo pelo ID.

    Raises:
        HTTPException 404 caso o veículo não exista.

    Returns:
        Veículo encontrado.
    """
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
    """
    Cria um novo veículo.

    Regras:
    - O cliente informado deve existir.
    - A placa deve ser única no sistema.
    """
    # Verifica se o cliente proprietário existe
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

    # Garante que não existem veículos com a mesma placa
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

    # Cria o registro do veículo após todas as validações
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

def listar_veiculos(
        db: Session
):
    """
    Retorna todos os veículos cadastrados.
    """
    veiculos = (
        db.query(Veiculo)
        .all()
    )

    return veiculos

def buscar_veiculo_por_id(
        db: Session,
        veiculo_id: int
):
    """
    Retorna um veículo específico pelo ID.
    """
    veiculo = obter_veiculo_ou_404(
        db,
        veiculo_id
    )

    return veiculo