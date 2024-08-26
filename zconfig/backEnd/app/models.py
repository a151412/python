from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Configuracao(Base):
    __tablename__ = "configuracoes"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date, index=True)
    cec = Column(String(8), index=True)
    memoria = Column(Integer)
    mips = Column(Integer)
    observacao = Column(String(100))
