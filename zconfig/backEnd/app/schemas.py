from pydantic import BaseModel
from datetime import date

class ConfiguracaoBase(BaseModel):
    data: date
    cec: str
    memoria: int
    mips: int
    observacao: str

class ConfiguracaoCreate(ConfiguracaoBase):
    pass

class Configuracao(ConfiguracaoBase):
    id: int

    class Config:
        from_attributes = True
