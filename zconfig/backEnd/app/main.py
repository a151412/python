from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy import asc, desc

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configurar os domínios permitidos
origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200",
    # Adicione outros domínios conforme necessário
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/configuracoes/latest", response_model=List[schemas.Configuracao])
def read_all_latest_configuracoes(db: Session = Depends(get_db)):
    configuracoes = []

    # Extrair valores de 'cec' como uma lista simples
    cecs = db.query(models.Configuracao.cec).distinct().all()
    cec_values = [row.cec for row in cecs]

    for cec in cec_values:
        latest_configuracao = db.query(models.Configuracao).filter(models.Configuracao.cec == cec).order_by(desc(models.Configuracao.data)).first()
        if latest_configuracao:
            configuracoes.append(latest_configuracao)

    return configuracoes

@app.get("/configuracoes/latest/{cec}", response_model=schemas.Configuracao)
def read_latest_configuracao(cec: str, db: Session = Depends(get_db)):
    db_configuracao = crud.get_latest_configuracao_by_cec(db, cec=cec)
    if db_configuracao is None:
        raise HTTPException(status_code=404, detail="Configuração não encontrada")
    return db_configuracao


@app.get("/configuracoes/oldest/{cec}", response_model=schemas.Configuracao)
def read_oldest_configuracao(cec: str, db: Session = Depends(get_db)):
    db_configuracao = crud.get_oldest_configuracao_by_cec(db, cec=cec)
    if db_configuracao is None:
        raise HTTPException(status_code=404, detail="Configuração não encontrada")
    return db_configuracao

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API!"}

@app.post("/configuracoes/", response_model=schemas.Configuracao)
def create_configuracao(configuracao: schemas.ConfiguracaoCreate, db: Session = Depends(get_db)):
    return crud.create_configuracao(db=db, configuracao=configuracao)

@app.get("/configuracoes/", response_model=list[schemas.Configuracao])
def read_configuracoes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    configuracoes = crud.get_configuracoes(db, skip=skip, limit=limit)
    return configuracoes

@app.get("/configuracoes/{configuracao_id}", response_model=schemas.Configuracao)
def read_configuracao(configuracao_id: int, db: Session = Depends(get_db)):
    db_configuracao = crud.get_configuracao(db, configuracao_id=configuracao_id)
    if db_configuracao is None:
        raise HTTPException(status_code=404, detail="Configuração não encontrada")
    return db_configuracao


