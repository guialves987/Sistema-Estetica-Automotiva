"""
Serviços responsáveis pelas regras de negócio relacionadas 
a clientes.

Esta camada concentra operações de criação, consulta, 
atualização e remoção de clientes 
"""

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
    """
    Cria um novo cliente no banco de dados

    Args:
        db: Sessão ativa do banco
        cliente: Dados do cliente a ser cadastrado

    Returns:
        Cliente criado
    """
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
    """
    Busca um cliente pelo ID.

    Raises:
        HTTPException 404 caso o cliente não exista.

    Returns:
        Cliente encontrado.
    """
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
    """
    Lista todos os clientes cadastrados.

    Caso um nome seja informado, realiza
    a busca parcial utilizando filtro.
    """
    query = db.query(Cliente)

    # Permite busca parcial por nome
    if nome:
        query = query.filter(
            Cliente.nome.ilike(f"%{nome}%")
        )

    return query.all()

def buscar_cliente_por_id(
    db: Session,
    cliente_id: int
):
    """
    Retorna um cliente específico pelo ID
    """
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
    """
    Atualiza os dados de um cliente existente
    """
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
    """
    Remove um cliente do sistema.

    Antes da remoção, exclui todos os veículos
    associados ao cliente para manter a integridade
    dos dados.
    """
    cliente = obter_cliente_ou_404(
        db,
        cliente_id
    )

    # Busca todos os veículos vinculados ao cliente
    veiculos = (
        db.query(Veiculo)
        .filter(
            Veiculo.cliente_id == cliente_id
        )
        .all()
    )

    # Remove os veículos antes de excluir o cliente
    for veiculo in veiculos:
        db.delete(veiculo)
    
    db.delete(cliente)
    db.commit()