"""
Aplicação FastAPI Principal
"""
from fastapi import FastAPI, HTTPException, Depends, Query, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime
import logging
import uvicorn
from config import settings
from database import init_db, get_db
from schemas import (
    FeiticoCreate, FeiticoUpdate, Feitico, Grimorio,
    ApiResponse, PaginatedResponse, GrimorioStats
)
from services import FeiticoService, GrimorioService

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Criar app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="API REST para gerenciar uma coleção de feitiços mágicos",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================================
# INICIALIZAÇÃO
# =====================================================================

@app.on_event("startup")
async def startup_event():
    """Executado ao iniciar a aplicação"""
    init_db()
    logger.info(f"🚀 {settings.APP_NAME} v{settings.APP_VERSION} iniciado")

# =====================================================================
# ENDPOINTS - HEALTH CHECK
# =====================================================================

@app.get("/health", tags=["Sistema"])
async def health_check():
    """Verificar saúde da API"""
    return {
        "status": "ok",
        "aplicacao": settings.APP_NAME,
        "versao": settings.APP_VERSION,
        "timestamp": datetime.utcnow().isoformat()
    }

# =====================================================================
# ENDPOINTS - FEITIÇOS
# =====================================================================

@app.get(f"{settings.API_PREFIX}/feiticos", response_model=PaginatedResponse, tags=["Feitiços"])
async def listar_feiticos(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    ordem: str = Query("nome", regex="^(nome|nivel|recente)$"),
    db: Session = Depends(get_db)
):
    """
    Listar todos os feitiços com paginação
    
    **Parâmetros de Query:**
    - `skip`: Número de registros a pular (padrão: 0)
    - `limit`: Número de registros a retornar (padrão: 20, máx: 100)
    - `ordem`: Campo de ordenação (nome, nivel ou recente)
    """
    try:
        feiticos, total = FeiticoService.listar_feiticos(db, skip, limit, ordem)
        
        total_paginas = (total + limit - 1) // limit
        
        return PaginatedResponse(
            itens=[Feitico.model_validate(f) for f in feiticos],
            total=total,
            pagina=skip // limit + 1,
            por_pagina=limit,
            total_paginas=total_paginas,
            sucesso=True,
            mensagem="Feitiços recuperados com sucesso"
        )
    except Exception as e:
        logger.error(f"Erro ao listar feitiços: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get(f"{settings.API_PREFIX}/feiticos/buscar", response_model=PaginatedResponse, tags=["Feitiços"])
async def buscar_feiticos(
    termo: str = Query(..., min_length=1),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    Buscar feitiços por nome
    
    **Parâmetros de Query:**
    - `termo`: Termo de busca (obrigatório)
    - `skip`: Número de registros a pular
    - `limit`: Número de registros a retornar
    """
    try:
        feiticos, total = FeiticoService.buscar_feiticos(db, termo, skip, limit)
        
        total_paginas = (total + limit - 1) // limit
        
        return PaginatedResponse(
            itens=[Feitico.model_validate(f) for f in feiticos],
            total=total,
            pagina=skip // limit + 1,
            por_pagina=limit,
            total_paginas=total_paginas,
            sucesso=True,
            mensagem=f"Encontrados {total} feitiço(s) com o termo '{termo}'"
        )
    except Exception as e:
        logger.error(f"Erro ao buscar feitiços: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get(f"{settings.API_PREFIX}/feiticos/escola", response_model=PaginatedResponse, tags=["Feitiços"])
async def filtrar_por_escola(
    escola: str = Query(..., min_length=1),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    Filtrar feitiços por escola de magia
    
    **Parâmetros de Query:**
    - `escola`: Nome da escola (obrigatório)
    - `skip`: Número de registros a pular
    - `limit`: Número de registros a retornar
    """
    try:
        feiticos, total = FeiticoService.filtrar_por_escola(db, escola, skip, limit)
        
        total_paginas = (total + limit - 1) // limit
        
        return PaginatedResponse(
            itens=[Feitico.model_validate(f) for f in feiticos],
            total=total,
            pagina=skip // limit + 1,
            por_pagina=limit,
            total_paginas=total_paginas,
            sucesso=True,
            mensagem=f"Encontrados {total} feitiço(s) da escola '{escola}'"
        )
    except Exception as e:
        logger.error(f"Erro ao filtrar por escola: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get(f"{settings.API_PREFIX}/feiticos/nivel", response_model=PaginatedResponse, tags=["Feitiços"])
async def filtrar_por_nivel(
    nivel: int = Query(..., ge=0, le=9),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    Filtrar feitiços por nível
    
    **Parâmetros de Query:**
    - `nivel`: Nível do feitiço (0-9, obrigatório)
    - `skip`: Número de registros a pular
    - `limit`: Número de registros a retornar
    """
    try:
        feiticos, total = FeiticoService.filtrar_por_nivel(db, nivel, skip, limit)
        
        total_paginas = (total + limit - 1) // limit
        
        return PaginatedResponse(
            itens=[Feitico.model_validate(f) for f in feiticos],
            total=total,
            pagina=skip // limit + 1,
            por_pagina=limit,
            total_paginas=total_paginas,
            sucesso=True,
            mensagem=f"Encontrados {total} feitiço(s) de nível {nivel}"
        )
    except Exception as e:
        logger.error(f"Erro ao filtrar por nível: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get(f"{settings.API_PREFIX}/feiticos/{{feitico_id}}", response_model=Feitico, tags=["Feitiços"])
async def obter_feitico(feitico_id: int, db: Session = Depends(get_db)):
    """
    Obter detalhes de um feitiço específico
    
    **Parâmetros de Path:**
    - `feitico_id`: ID único do feitiço
    """
    try:
        feitico = FeiticoService.obter_feitico_por_id(db, feitico_id)
        
        if not feitico:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Feitiço com ID {feitico_id} não encontrado"
            )
        
        return Feitico.model_validate(feitico)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro ao obter feitiço: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post(f"{settings.API_PREFIX}/feiticos", response_model=Feitico, status_code=status.HTTP_201_CREATED, tags=["Feitiços"])
async def criar_feitico(feitico_in: FeiticoCreate, db: Session = Depends(get_db)):
    """
    Criar um novo feitiço
    
    **Body:**
    - `nome` (obrigatório): Nome do feitiço
    - `nivel`: Nível (0-9)
    - `escola`: Escola de magia
    - `tempo`: Tempo de conjuração
    - `alcance`: Alcance do feitiço
    - `componentes`: Componentes necessários
    - `duracao`: Duração do efeito
    - `descricao`: Descrição detalhada
    """
    try:
        # Verificar se feitiço já existe
        existente = FeiticoService.obter_feitico_por_nome(db, feitico_in.nome)
        if existente:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Feitiço '{feitico_in.nome}' já existe"
            )
        
        feitico = FeiticoService.criar_feitico(db, feitico_in)
        return Feitico.model_validate(feitico)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro ao criar feitiço: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.put(f"{settings.API_PREFIX}/feiticos/{{feitico_id}}", response_model=Feitico, tags=["Feitiços"])
async def atualizar_feitico(
    feitico_id: int,
    feitico_update: FeiticoUpdate,
    db: Session = Depends(get_db)
):
    """
    Atualizar um feitiço existente
    
    **Parâmetros de Path:**
    - `feitico_id`: ID único do feitiço
    """
    try:
        feitico = FeiticoService.atualizar_feitico(db, feitico_id, feitico_update)
        
        if not feitico:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Feitiço com ID {feitico_id} não encontrado"
            )
        
        return Feitico.model_validate(feitico)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro ao atualizar feitiço: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.delete(f"{settings.API_PREFIX}/feiticos/{{feitico_id}}", status_code=status.HTTP_204_NO_CONTENT, tags=["Feitiços"])
async def deletar_feitico(feitico_id: int, db: Session = Depends(get_db)):
    """
    Deletar um feitiço
    
    **Parâmetros de Path:**
    - `feitico_id`: ID único do feitiço
    """
    try:
        sucesso = FeiticoService.deletar_feitico(db, feitico_id)
        
        if not sucesso:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Feitiço com ID {feitico_id} não encontrado"
            )
        
        return None
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro ao deletar feitiço: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# =====================================================================
# ENDPOINTS - GRIMÓRIO
# =====================================================================

@app.get(f"{settings.API_PREFIX}/grimorio", response_model=Grimorio, tags=["Grimório"])
async def obter_grimorio(db: Session = Depends(get_db)):
    """
    Obter informações do grimório principal
    """
    try:
        grimorio = GrimorioService.obter_grimorio_padrao(db)
        return Grimorio.model_validate(grimorio)
    except Exception as e:
        logger.error(f"Erro ao obter grimório: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get(f"{settings.API_PREFIX}/grimorio/stats", tags=["Grimório"])
async def obter_stats(db: Session = Depends(get_db)):
    """
    Obter estatísticas do grimório
    """
    try:
        stats = GrimorioService.get_stats(db)
        
        return ApiResponse(
            sucesso=True,
            dados=stats,
            mensagem="Estatísticas recuperadas com sucesso",
            codigo=200
        )
    except Exception as e:
        logger.error(f"Erro ao obter estatísticas: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# =====================================================================
# RAIZ
# =====================================================================

@app.get("/", tags=["Info"])
async def root():
    """Informações da API"""
    return {
        "nome": settings.APP_NAME,
        "versao": settings.APP_VERSION,
        "descricao": "API REST para gerenciar feitiços mágicos",
        "docs": "/docs",
        "redoc": "/redoc",
        "health": "/health"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
