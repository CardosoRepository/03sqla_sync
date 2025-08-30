from typing import Optional

from sqlmodel import Field, SQLModel

from datetime import datetime

class AditivoNutritivo(SQLModel, table=True):
    __tablename__ = 'aditivos_nutritivos'

    id:              Optional[int] = Field(default=None, primary_key=True, autoincrement=True)
    data_criacao:    datetime      = Field(default=datetime.now, index=True)
    nome:            str           = Field(max_length=45, unique=True)
    formula_quimica: str           = Field(max_length=100, unique=True)

    def __repr__(self) -> str:
        return f'<AditivoNutritivo: {self.nome}>'
    
    