from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from . import models, schemas

def get_configuracao(db: Session, configuracao_id: int):
    return db.query(models.Configuracao).filter(models.Configuracao.id == configuracao_id).first()

def get_configuracoes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Configuracao).offset(skip).limit(limit).all()

def create_configuracao(db: Session, configuracao: schemas.ConfiguracaoCreate):
    db_configuracao = models.Configuracao(**configuracao.dict())
    db.add(db_configuracao)
    db.commit()
    db.refresh(db_configuracao)
    return db_configuracao

def get_oldest_configuracao_by_cec(db: Session, cec: str):
    return db.query(models.Configuracao).filter(models.Configuracao.cec == cec).order_by(asc(models.Configuracao.data)).first()

def get_latest_configuracao_by_cec(db: Session, cec: str):
    return db.query(models.Configuracao).filter(models.Configuracao.cec == cec).order_by(desc(models.Configuracao.data)).first()
