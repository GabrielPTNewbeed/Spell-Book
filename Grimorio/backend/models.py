"""
Modelos SQLAlchemy para persistência de dados
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

# Tabela de associação para relacionamento many-to-many
grimorio_feiticos = Table(
    'grimorio_feiticos',
    Base.metadata,
    Column('grimorio_id', Integer, ForeignKey('grimorios.id'), primary_key=True),
    Column('feitico_id', Integer, ForeignKey('feiticos.id'), primary_key=True)
)

class GrimorioModel(Base):
    """Modelo SQLAlchemy para Grimório"""
    __tablename__ = "grimorios"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(200), unique=True, nullable=False, index=True)
    descricao = Column(Text, nullable=True)
    criado_em = Column(DateTime, default=datetime.utcnow, nullable=False)
    atualizado_em = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relacionamento
    feiticos = relationship(
        "FeiticoModel",
        secondary=grimorio_feiticos,
        back_populates="grimorios"
    )
    
    def __repr__(self):
        return f"<Grimorio(id={self.id}, nome='{self.nome}', total_feiticos={len(self.feiticos)})>"

class FeiticoModel(Base):
    """Modelo SQLAlchemy para Feitiço"""
    __tablename__ = "feiticos"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), unique=True, nullable=False, index=True)
    nivel = Column(Integer, default=0, nullable=False, index=True)
    escola = Column(String(100), nullable=True, index=True)
    tempo = Column(String(100), nullable=True)
    alcance = Column(String(100), nullable=True)
    componentes = Column(Text, nullable=True)
    duracao = Column(String(100), nullable=True)
    descricao = Column(Text, nullable=True)
    criado_em = Column(DateTime, default=datetime.utcnow, nullable=False)
    atualizado_em = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relacionamento
    grimorios = relationship(
        "GrimorioModel",
        secondary=grimorio_feiticos,
        back_populates="feiticos"
    )
    
    def __repr__(self):
        return f"<Feitico(id={self.id}, nome='{self.nome}', nivel={self.nivel}, escola='{self.escola}')>"
