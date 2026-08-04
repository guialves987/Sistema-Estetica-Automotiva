"""
Centraliza a importação dos modelos da aplicação.

Permite que o SQLAlchemy e o Alembic identifiquem todas
as entidades registradas no sistema.
"""

from app.models.cliente import Cliente
from app.models.veiculo import Veiculo