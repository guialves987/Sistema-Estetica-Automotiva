"""
Configuração da conexão com o banco de dados.

Responsável por:
- Criar o engine de conexão.
- Configurar a fábrica de sessões.
- Disponibilizar sessões para as rotas da aplicação.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Cria o mecanismo de conexão com banco de dados
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Fábrica de sessões utilizada para interagir com o banco
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    """
    Fornece uma sessão do banco de dados para as rotas.

    Utiliza o padrão de dependência do FastAPI para garantir
    que a sessão seja encerrada corretamente ao final de cada
    requisição.

    Yields:
        Session: Sessão ativa do banco de dados.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        # Garante o fechamento da conexão após o uso
        db.close()