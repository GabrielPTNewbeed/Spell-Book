"""
Modelos Pydantic para validação de dados (Contrato JSON)
"""
from pydantic import BaseModel, Field, validator
from typing import Optional, Dict, Union, List
from datetime import datetime
from enum import Enum

class EscolaEnum(str, Enum):
    """Escolas de magia válidas"""
    ABJURACAO = "Abjuração"
    CONJURACAO = "Conjuração"
    DIVINACAO = "Divinação"
    ENCANTAMENTO = "Encantamento"
    EVOCACAO = "Evocação"
    ILUSAO = "Ilusão"
    NECROMANCIA = "Necromancia"
    TRANSMUTACAO = "Transmutação"

class FeiticoBase(BaseModel):
    """Modelo base para Feitiço"""
    nome: str = Field(..., min_length=1, max_length=100, description="Nome do feitiço")
    nivel: int = Field(default=0, ge=0, le=9, description="Nível do feitiço (0-9)")
    escola: Optional[str] = Field(default=None, max_length=100, description="Escola de magia")
    tempo: Optional[str] = Field(default=None, max_length=100, description="Tempo de conjuração")
    alcance: Optional[str] = Field(default=None, max_length=100, description="Alcance do feitiço")
    componentes: Optional[str] = Field(default=None, max_length=500, description="Componentes necessários")
    duracao: Optional[str] = Field(default=None, max_length=100, description="Duração do efeito")
    descricao: Optional[str] = Field(default=None, max_length=5000, description="Descrição detalhada")
    
    @validator('nome')
    def nome_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Nome não pode ser vazio')
        return v.strip()

class FeiticoCreate(FeiticoBase):
    """Modelo para criar novo feitiço"""
    pass

class FeiticoUpdate(BaseModel):
    """Modelo para atualizar feitiço"""
    nome: Optional[str] = Field(None, min_length=1, max_length=100)
    nivel: Optional[int] = Field(None, ge=0, le=9)
    escola: Optional[str] = Field(None, max_length=100)
    tempo: Optional[str] = Field(None, max_length=100)
    alcance: Optional[str] = Field(None, max_length=100)
    componentes: Optional[str] = Field(None, max_length=500)
    duracao: Optional[str] = Field(None, max_length=100)
    descricao: Optional[str] = Field(None, max_length=5000)

class Feitico(FeiticoBase):
    """Modelo de Feitiço com metadados"""
    id: int = Field(..., description="ID único do feitiço")
    criado_em: datetime = Field(..., description="Timestamp de criação")
    atualizado_em: datetime = Field(..., description="Timestamp da última atualização")
    
    class Config:
        from_attributes = True

class GrimorioBase(BaseModel):
    """Modelo base para Grimório"""
    nome: str = Field(..., min_length=1, max_length=200, description="Nome do grimório")
    descricao: Optional[str] = Field(None, max_length=1000, description="Descrição do grimório")

class GrimorioCreate(GrimorioBase):
    """Modelo para criar novo grimório"""
    pass

class GrimorioStats(BaseModel):
    """Estatísticas do grimório"""
    total_feiticos: int
    feiticos_por_nivel: Dict[int, int]
    feiticos_por_escola: Dict[str, int]
    data_atualizacao: datetime

class Grimorio(GrimorioBase):
    """Modelo de Grimório com metadados"""
    id: int
    criado_em: datetime
    atualizado_em: datetime
    total_feiticos: int
    
    class Config:
        from_attributes = True

class ApiResponse(BaseModel):
    """Resposta padrão de API"""
    sucesso: bool = Field(..., description="Indica se a operação foi bem-sucedida")
    dados: Optional[Union[dict, list]] = Field(None, description="Dados da resposta")
    mensagem: str = Field(..., description="Mensagem descritiva")
    codigo: int = Field(..., description="Código HTTP")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Timestamp da resposta")

class PaginatedResponse(BaseModel):
    """Resposta paginada"""
    itens: List = Field(default_factory=list, description="Lista de itens paginados")
    total: int
    pagina: int
    por_pagina: int
    total_paginas: int
    sucesso: bool = True
    mensagem: str = "Ok"
    timestamp: datetime = Field(default_factory=datetime.utcnow)
