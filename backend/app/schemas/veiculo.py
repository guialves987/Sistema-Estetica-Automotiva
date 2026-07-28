from pydantic import BaseModel

class ClienteVeiculoResponse(BaseModel):
    id: int
    nome: str

    model_config = {
        "from_attributes": True
    }

class VeiculoBase(BaseModel):
    cliente_id: int
    placa: str
    marca: str
    modelo: str
    ano: int | None = None
    cor: str | None = None
    observacoes: str | None = None

class VeiculoCreate(VeiculoBase):
    pass

class VeiculoUpdate(VeiculoBase):
    pass

class VeiculoResponse(BaseModel):
    id: int
    placa: str
    marca: str
    modelo: str
    ano: int | None = None
    cor: str | None = None
    observacoes: str | None = None

    cliente: ClienteVeiculoResponse

    model_config = {
        "from_attributes": True
    }