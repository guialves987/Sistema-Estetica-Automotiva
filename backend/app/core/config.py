"""
Configurações gerais da aplicação.

Responsável por carregar variáveis de ambiente e definir
valores padrão utilizados pelo sistema.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
     de configurações da aplicação.

    Os valores podem ser carregados de um arquivo .env
    ou utilizar os valores padrão definidos abaixo.
    """

    # Nome da aplicação exibido na documentação da API
    APP_NAME: str = "Sistema Na Garagem"

    # Versão atual da aplicação
    VERSION: str = "0.1.0"

    # URL de conexão com banco de dados
    DATABASE_URL: str = "sqlite:///data/estetica.db"

    # Configuração do pydantic settings
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

# Instância única das configurações utilizada em toda a aplicação
settings = Settings()