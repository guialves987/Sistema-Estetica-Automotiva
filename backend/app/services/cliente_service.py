from sqlalchemy.orm import Session

from app.models.cliente import Cliente
from app.schemas.cliente import (
    ClienteCreate,
    ClienteUpdate
)

from app.models.veiculo import Veiculo

from fastapi import HTTPException

def criar_cliente(
        db: Session,
        cliente: ClienteCreate
) -> Cliente:
    
    novo_cliente = Cliente(
        nome=cliente.nome,
        telefone=cliente.telefone,
        observacoes=cliente.observacoes
    )

    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)

    return novo_cliente

def obter_cliente_ou_404(
        db: Session,
        cliente_id: int
) -> Cliente:
    cliente = (
        db.query(Cliente)
        .filter(Cliente.id == cliente_id)
        .first()
    )

    if not cliente:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )
    
    return cliente

def listar_clientes(
        db: Session,
        nome: str | None = None
):
    query = db.query(Cliente)

    if nome:
        query = query.filter(
            Cliente.nome.ilike(f"%{nome}%")
        )

    return query.all()

def buscar_cliente_por_id(
    db: Session,
    cliente_id: int
):
    cliente = obter_cliente_ou_404(
        db,
        cliente_id
    )
    
    return cliente

def atualizar_cliente(
    db: Session,
    cliente_id: int,
    dados: ClienteUpdate
):
    cliente = obter_cliente_ou_404(
        db,
        cliente_id
    )
    
    cliente.nome = dados.nome
    cliente.telefone = dados.telefone
    cliente.observacoes = dados.observacoes

    db.commit()
    db.refresh(cliente)

    return cliente

def deletar_cliente(
    db: Session,
    cliente_id: int
):
    cliente = obter_cliente_ou_404(
        db,
        cliente_id
    )

    veiculos = (
        db.query(Veiculo)
        .filter(
            Veiculo.cliente_id == cliente_id
        )
        .all()
    )

    for veiculo in veiculos:
        db.delete(veiculo)
    
    db.delete(cliente)
    db.commit()