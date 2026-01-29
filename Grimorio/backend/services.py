"""
Serviços de Negócio para Feitiços
"""
from sqlalchemy.orm import Session
from models import FeiticoModel, GrimorioModel
from schemas import FeiticoCreate, FeiticoUpdate
from datetime import datetime
from typing import Optional, Tuple
import logging

logger = logging.getLogger(__name__)

class FeiticoService:
    """Serviço para operações com feitiços"""
    
    @staticmethod
    def criar_feitico(db: Session, feitico_in: FeiticoCreate) -> FeiticoModel:
        """Cria um novo feitiço"""
        db_feitico = FeiticoModel(
            nome=feitico_in.nome,
            nivel=feitico_in.nivel,
            escola=feitico_in.escola,
            tempo=feitico_in.tempo,
            alcance=feitico_in.alcance,
            componentes=feitico_in.componentes,
            duracao=feitico_in.duracao,
            descricao=feitico_in.descricao
        )
        db.add(db_feitico)
        db.commit()
        db.refresh(db_feitico)
        logger.info(f"Feitiço '{db_feitico.nome}' criado com sucesso")
        return db_feitico
    
    @staticmethod
    def obter_feitico_por_id(db: Session, feitico_id: int) -> Optional[FeiticoModel]:
        """Obtém um feitiço pelo ID"""
        return db.query(FeiticoModel).filter(FeiticoModel.id == feitico_id).first()
    
    @staticmethod
    def obter_feitico_por_nome(db: Session, nome: str) -> Optional[FeiticoModel]:
        """Obtém um feitiço pelo nome"""
        return db.query(FeiticoModel).filter(FeiticoModel.nome == nome).first()
    
    @staticmethod
    def listar_feiticos(
        db: Session, 
        skip: int = 0, 
        limit: int = 20,
        ordem: str = "nome"
    ) -> Tuple[list, int]:
        """Lista todos os feitiços com paginação"""
        query = db.query(FeiticoModel)
        
        # Ordenação
        if ordem == "nome":
            query = query.order_by(FeiticoModel.nome)
        elif ordem == "nivel":
            query = query.order_by(FeiticoModel.nivel)
        elif ordem == "recente":
            query = query.order_by(FeiticoModel.atualizado_em.desc())
        
        total = query.count()
        feiticos = query.offset(skip).limit(limit).all()
        
        return feiticos, total
    
    @staticmethod
    def buscar_feiticos(
        db: Session,
        termo: str,
        skip: int = 0,
        limit: int = 20
    ) -> Tuple[list, int]:
        """Busca feitiços por nome"""
        query = db.query(FeiticoModel).filter(
            FeiticoModel.nome.ilike(f"%{termo}%")
        ).order_by(FeiticoModel.nome)
        
        total = query.count()
        feiticos = query.offset(skip).limit(limit).all()
        
        return feiticos, total
    
    @staticmethod
    def filtrar_por_escola(
        db: Session,
        escola: str,
        skip: int = 0,
        limit: int = 20
    ) -> Tuple[list, int]:
        """Filtra feitiços por escola"""
        query = db.query(FeiticoModel).filter(
            FeiticoModel.escola.ilike(f"%{escola}%")
        ).order_by(FeiticoModel.nome)
        
        total = query.count()
        feiticos = query.offset(skip).limit(limit).all()
        
        return feiticos, total
    
    @staticmethod
    def filtrar_por_nivel(
        db: Session,
        nivel: int,
        skip: int = 0,
        limit: int = 20
    ) -> Tuple[list, int]:
        """Filtra feitiços por nível"""
        query = db.query(FeiticoModel).filter(
            FeiticoModel.nivel == nivel
        ).order_by(FeiticoModel.nome)
        
        total = query.count()
        feiticos = query.offset(skip).limit(limit).all()
        
        return feiticos, total
    
    @staticmethod
    def atualizar_feitico(
        db: Session,
        feitico_id: int,
        feitico_update: FeiticoUpdate
    ) -> Optional[FeiticoModel]:
        """Atualiza um feitiço"""
        db_feitico = db.query(FeiticoModel).filter(FeiticoModel.id == feitico_id).first()
        
        if not db_feitico:
            return None
        
        # Atualizar apenas campos fornecidos
        update_data = feitico_update.model_dump(exclude_unset=True)
        for campo, valor in update_data.items():
            setattr(db_feitico, campo, valor)
        
        db_feitico.atualizado_em = datetime.utcnow()
        db.add(db_feitico)
        db.commit()
        db.refresh(db_feitico)
        
        logger.info(f"Feitiço '{db_feitico.nome}' atualizado com sucesso")
        return db_feitico
    
    @staticmethod
    def deletar_feitico(db: Session, feitico_id: int) -> bool:
        """Deleta um feitiço"""
        db_feitico = db.query(FeiticoModel).filter(FeiticoModel.id == feitico_id).first()
        
        if not db_feitico:
            return False
        
        nome = db_feitico.nome
        db.delete(db_feitico)
        db.commit()
        
        logger.info(f"Feitiço '{nome}' deletado com sucesso")
        return True
    
    @staticmethod
    def contar_feiticos(db: Session) -> int:
        """Conta o total de feitiços"""
        return db.query(FeiticoModel).count()

class GrimorioService:
    """Serviço para operações com grimórios"""
    
    @staticmethod
    def criar_grimorio(db: Session, nome: str, descricao: Optional[str] = None) -> GrimorioModel:
        """Cria um novo grimório"""
        db_grimorio = GrimorioModel(
            nome=nome,
            descricao=descricao
        )
        db.add(db_grimorio)
        db.commit()
        db.refresh(db_grimorio)
        logger.info(f"Grimório '{db_grimorio.nome}' criado com sucesso")
        return db_grimorio
    
    @staticmethod
    def obter_grimorio_padrao(db: Session) -> GrimorioModel:
        """Obtém ou cria o grimório padrão"""
        grimorio = db.query(GrimorioModel).filter(GrimorioModel.nome == "Grimório Principal").first()
        
        if not grimorio:
            grimorio = GrimorioService.criar_grimorio(
                db, 
                "Grimório Principal",
                "Grimório principal da coleção de mágica"
            )
        
        return grimorio
    
    @staticmethod
    def get_stats(db: Session, grimorio_id: Optional[int] = None) -> dict:
        """Obtém estatísticas do grimório"""
        if grimorio_id:
            grimorio = db.query(GrimorioModel).filter(GrimorioModel.id == grimorio_id).first()
            if not grimorio:
                return {}
            
            feiticos = grimorio.feiticos
        else:
            feiticos = db.query(FeiticoModel).all()
        
        # Contar por nível
        por_nivel = {}
        for f in feiticos:
            nivel = f.nivel or 0
            por_nivel[nivel] = por_nivel.get(nivel, 0) + 1
        
        # Contar por escola
        por_escola = {}
        for f in feiticos:
            escola = f.escola or "Sem Escola"
            por_escola[escola] = por_escola.get(escola, 0) + 1
        
        return {
            "total_feiticos": len(feiticos),
            "feiticos_por_nivel": por_nivel,
            "feiticos_por_escola": por_escola
        }
