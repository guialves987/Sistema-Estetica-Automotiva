"""
Modelo responsável por representar os veículos cadastrados
no sistema.

Todo veículo deve estar associado a um cliente.
"""

from sqlalchemy import (
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base

class Veiculo(Base):
    """
    Entidade que representa um veículo pertencente a um cliente.
    """

    __tablename__ = "veiculos"
    
    id: Mapped[int] = mapped_column(
            Integer,
            primary_key=True,
            index=True
        )

    # Referência ao proprietário do veículo
    cliente_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("clientes.id"),
        nullable=False
    )

    # Placa única utilizada para identificar o veículo
    placa: Mapped[str] = mapped_column(
        String(10),
        unique=True,
        nullable=False,
        index=True
    )

    marca: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    modelo: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    ano: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    cor: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True
    )

    observacoes: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    # Relacionamento N:1 com cliente
    cliente = relationship(
        "Cliente",
        back_populates="veiculos"
    )