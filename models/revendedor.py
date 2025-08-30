from typing import Optional

from sqlmodel import Field, SQLModel

from datetime import datetime

class Revendedor(SQLModel, table=True):
    __tablename__ = 'revendedores'

    id:           Optional[int] = Field(primary_key=True, autoincrement=True)
    data_criacao: datetime      = Field(default=datetime.now, index=True)
    cnpj:         str           = Field(max_length=45, unique=True)
    razao_social: str           = Field(max_length=100)
    contato:      str           = Field(max_length=100)

    def __repr__(self) -> str:
        return f'<Revendedor: {self.razao_social}>'
    
    