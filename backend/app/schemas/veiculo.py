"""
Schemas utilizados nas operações relacionadas a veículos.

Responsáveis por validar os dados recebidos pela API
e definir o formato das respostas enviadas ao cliente.
"""

from pydantic import BaseModel

class ClienteVeiculoResponse(BaseModel):
    """
    Schema simplificado de cliente utilizado
    dentro das respostas de veículos.
    """

    id: int
    nome: str

    model_config = {
        "from_attributes": True
    }

class VeiculoBase(BaseModel):
    """
    Schema base compartilhado entre criação
    e atualização de veículos.
    """

    cliente_id: int
    placa: str
    marca: str
    modelo: str
    ano: int | None = None
    cor: str | None = None
    observacoes: str | None = None

class VeiculoCreate(VeiculoBase):
    """
    Schema utilizado para criação de veículos.
    """
    pass

class VeiculoUpdate(VeiculoBase):
    """
    Schema utilizado para atualização de veículos.
    """
    pass

class VeiculoResponse(BaseModel):
    """
    Schema utilizado nas respostas da API
    contendo os dados completos do veículo
    e do respectivo proprietário.
    """

    id: int
    placa: str
    marca: str
    modelo: str
    ano: int | None = None
    cor: str | None = None
    observacoes: str | None = None

    # Dados resumidos do cliente proprietário
    cliente: ClienteVeiculoResponse

    model_config = {
        "from_attributes": True
    }