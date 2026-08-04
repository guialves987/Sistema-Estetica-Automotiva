"""
Classe base utilizada por todos os modelos da aplicação.

Centraliza a herança dos modelos SQLAlchemy e permite que
o Alembic identifique automaticamente as tabelas durante
a geração das migrações.
"""

from sqlalchemy.orm import DeclarativeBase

# Classe base para todos os modelos ORM do sistema
class Base(DeclarativeBase):
    pass