from datetime import datetime

from sqlalchemy import DateTime, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class Cliente(Base):
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

    data_criacao: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    veiculos = relationship(
        "Veiculo",
        back_populates="cliente"
    )