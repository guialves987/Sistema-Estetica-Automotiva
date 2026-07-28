from sqlalchemy import (
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base

class Veiculo(Base):
    __tablename__ = "veiculos"
    
    id: Mapped[int] = mapped_column(
            Integer,
            primary_key=True,
            index=True
        )

    cliente_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("clientes.id"),
        nullable=False
    )

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

    cliente = relationship(
        "Cliente",
        back_populates="veiculos"
    )