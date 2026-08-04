"""
Modelo responsável por representar os clientes cadastrados
no sistema.

Um cliente pode possuir um ou mais veículos associados.
"""

from datetime import datetime

from sqlalchemy import DateTime, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class Cliente(Base):
    """
    Entidade que representa um cliente da empresa.
    """

    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    telefone: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    observacoes: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    # Data de criação automática do registro
    data_criacao: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    # Relacionamento 1:N entre cliente e veículos
    veiculos = relationship(
        "Veiculo",
        back_populates="cliente"
    )