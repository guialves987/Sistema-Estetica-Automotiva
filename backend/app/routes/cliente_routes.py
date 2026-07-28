from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.cliente import (
    ClienteCreate,
    ClienteResponse,
    ClienteUpdate,
)

from app.services.cliente_service import (
    criar_cliente,
    listar_clientes,
    buscar_cliente_por_id,
    atualizar_cliente,
    deletar_cliente
)

from typing import Optional



router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

@router.post(
    "/",
    response_model=ClienteResponse
)
def criar_cliente_endpoint(
    cliente: ClienteCreate,
    db: Session = Depends(get_db)
):
    return criar_cliente(
        db=db,
        cliente=cliente
    )

@router.get(
    "/",
    response_model=list[ClienteResponse]
)
def listar_clientes_endpoint(
    nome: Optional[str] = None,
    db: Session = Depends(get_db)
):
    return listar_clientes(
        db=db,
        nome=nome
    )

@router.get(
    "/{cliente_id}",
    response_model=ClienteResponse
)
def buscar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db)
):
    return buscar_cliente_por_id(
        db,
        cliente_id
    )

@router.put(
    "/{cliente_id}",
    response_model=ClienteResponse
)
def atualizar_cliente_endpoint(
    cliente_id: int,
    dados: ClienteUpdate,
    db: Session = Depends(get_db)
):
    return atualizar_cliente(
        db,
        cliente_id,
        dados
    )   

@router.delete("/{cliente_id}", status_code=204)
def deletar_cliente_endpoint(
    cliente_id: int,
    db: Session = Depends(get_db)
):
    deletar_cliente(db, cliente_id)