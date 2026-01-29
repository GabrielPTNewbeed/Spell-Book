"""
Script para migrar dados do formato antigo JSON/SQLite para novo banco de dados
"""
import json
import sqlite3
from datetime import datetime
from sqlalchemy.orm import Session
from models import FeiticoModel
from database import SessionLocal, init_db
import logging
import os
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def migrar_do_json(arquivo_json: str, db: Session):
    """Migra dados do arquivo JSON antigo"""
    try:
        if not os.path.exists(arquivo_json):
            logger.warning(f"Arquivo JSON não encontrado: {arquivo_json}")
            return 0
        
        with open(arquivo_json, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        total = 0
        for nome, dados_feitico in dados.items():
            try:
                # Verificar se já existe
                existente = db.query(FeiticoModel).filter(
                    FeiticoModel.nome == nome
                ).first()
                
                if existente:
                    logger.info(f"Feitiço '{nome}' já existe, pulando...")
                    continue
                
                # Converter nível
                nivel = 0
                try:
                    nivel_str = str(dados_feitico.get('nível', '0')).strip()
                    if nivel_str.isdigit():
                        nivel = int(nivel_str)
                except (ValueError, TypeError):
                    nivel = 0
                
                feitico = FeiticoModel(
                    nome=nome,
                    nivel=nivel,
                    escola=dados_feitico.get('escola', ''),
                    tempo=dados_feitico.get('tempo', ''),
                    alcance=dados_feitico.get('alcance', ''),
                    componentes=dados_feitico.get('componentes', ''),
                    duracao=dados_feitico.get('duração', ''),
                    descricao=dados_feitico.get('descrição', ''),
                    criado_em=datetime.utcnow(),
                    atualizado_em=datetime.utcnow()
                )
                
                db.add(feitico)
                total += 1
                
            except Exception as e:
                logger.error(f"Erro ao migrar feitiço '{nome}': {e}")
        
        db.commit()
        logger.info(f"✅ {total} feitiços migrados do JSON com sucesso")
        return total
        
    except Exception as e:
        logger.error(f"Erro ao migrar JSON: {e}")
        db.rollback()
        return 0

def migrar_do_sqlite_antigo(arquivo_db: str, db: Session):
    """Migra dados do banco SQLite antigo"""
    try:
        if not os.path.exists(arquivo_db):
            logger.warning(f"Arquivo SQLite não encontrado: {arquivo_db}")
            return 0
        
        # Conectar ao banco antigo
        conexao_antiga = sqlite3.connect(arquivo_db)
        conexao_antiga.row_factory = sqlite3.Row
        cursor = conexao_antiga.cursor()
        
        # Buscar dados da tabela spells
        cursor.execute("SELECT * FROM spells")
        linhas = cursor.fetchall()
        
        total = 0
        for linha in linhas:
            try:
                # Verificar se já existe
                existente = db.query(FeiticoModel).filter(
                    FeiticoModel.nome == linha['nome']
                ).first()
                
                if existente:
                    logger.info(f"Feitiço '{linha['nome']}' já existe, pulando...")
                    continue
                
                feitico = FeiticoModel(
                    nome=linha['nome'],
                    nivel=linha.get('nivel') or 0,
                    escola=linha.get('escola') or '',
                    tempo=linha.get('tempo') or '',
                    alcance=linha.get('alcance') or '',
                    componentes=linha.get('componentes') or '',
                    duracao=linha.get('duracao') or '',
                    descricao=linha.get('descricao') or '',
                    criado_em=datetime.utcnow(),
                    atualizado_em=datetime.utcnow()
                )
                
                db.add(feitico)
                total += 1
                
            except Exception as e:
                logger.error(f"Erro ao migrar feitiço: {e}")
        
        conexao_antiga.close()
        db.commit()
        logger.info(f"✅ {total} feitiços migrados do SQLite antigo com sucesso")
        return total
        
    except Exception as e:
        logger.error(f"Erro ao migrar SQLite: {e}")
        db.rollback()
        return 0

def main():
    """Executa a migração"""
    logger.info("🔄 Iniciando migração de dados...")
    
    # Inicializar novo banco
    init_db()
    
    # Criar sessão
    db = SessionLocal()
    
    try:
        total_migrado = 0
        
        # Tentar migrar do JSON
        total_migrado += migrar_do_json("../grimorio.json", db)
        
        # Tentar migrar do SQLite antigo
        total_migrado += migrar_do_sqlite_antigo("../grimorio.db", db)
        
        if total_migrado > 0:
            logger.info(f"✨ Migração concluída! Total de {total_migrado} feitiços importados")
        else:
            logger.info("ℹ️  Nenhum dado para migrar encontrado")
        
    finally:
        db.close()

if __name__ == "__main__":
    main()
