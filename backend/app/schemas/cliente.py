from datetime import datetime

from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nome: str
    telefone: str
    observacoes: str | None = None

class ClienteResponse(BaseModel):
    id: int
    nome: str
    telefone: str
    observacoes: str | None
    data_criacao: datetime

    model_config = {
        "from_attributes": True
    }

class ClienteUpdate(BaseModel):
    nome: str
    telefone: str
    observacoes: str | None = None