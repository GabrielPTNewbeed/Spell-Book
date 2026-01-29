"""
Gerenciador de Banco de Dados
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import logging
import os
from config import settings
from models import Base

logger = logging.getLogger(__name__)

# Verificar se é SQLite e criar diretório se necessário
if "sqlite" in settings.DATABASE_URL:
    db_dir = os.path.dirname(settings.DATABASE_URL.replace("sqlite:///", ""))
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir)

# Criar engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.SQLALCHEMY_ECHO,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    """Dependency para obter sessão do banco de dados"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Inicializa o banco de dados com as tabelas"""
    Base.metadata.create_all(bind=engine)
    logger.info("Banco de dados inicializado com sucesso")

def drop_db():
    """Remove todas as tabelas (apenas para desenvolvimento!)"""
    Base.metadata.drop_all(bind=engine)
    logger.warning("Todas as tabelas foram removidas")

def reset_db():
    """Reseta o banco de dados"""
    drop_db()
    init_db()
    logger.info("Banco de dados foi resetado")
