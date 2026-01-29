"""
Grimório Mágico - Configurações da Aplicação
"""
from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """Configurações gerais da aplicação"""
    
    # Aplicação
    APP_NAME: str = "Grimório Mágico API"
    APP_VERSION: str = "2.0.0"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # API
    API_PREFIX: str = "/api/v1"
    CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:5173"]
    
    # Banco de Dados
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "sqlite:///./grimorio.db"
    )
    SQLALCHEMY_ECHO: bool = DEBUG
    
    # JWT
    SECRET_KEY: str = os.getenv(
        "SECRET_KEY", 
        "sua-chave-secreta-aqui-mude-em-producao"
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/api.log"
    
    # Paginação
    ITEMS_PER_PAGE: int = 20
    
    # Backup
    BACKUP_ENABLED: bool = True
    BACKUP_DIR: str = "backups"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
