"""
Schemas utilizados nas operações relacionadas a clientes.

Responsáveis por validar os dados recebidos pela API
e definir o formato das respostas enviadas ao cliente.
"""

from datetime import datetime

from pydantic import BaseModel

class ClienteBase(BaseModel):
    """
    Schema base compartilhado entre criação
    e atualização de clientes.
    """
     
    nome: str
    telefone: str
    observacoes: str | None = None

class ClienteCreate(ClienteBase):
    """
    Schema utilizado para criação de clientes.
    """
    pass

class ClienteResponse(BaseModel):
    """
    Schema utilizado nas respostas da API
    contendo os dados completos de um cliente.
    """

    id: int
    nome: str
    telefone: str
    observacoes: str | None
    data_criacao: datetime

    model_config = {
        "from_attributes": True
    }

class ClienteUpdate(ClienteBase):
    """
    Schema utilizado para atualização
    dos dados de um cliente.
    """
    pass