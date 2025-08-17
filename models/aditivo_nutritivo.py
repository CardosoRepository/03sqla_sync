import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
from typing import List

from models.model_base import ModelBase

class AditivoNutritivo(ModelBase):
    __tablename__ = 'aditivos_nutritivos'

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now, index=True)
    nome: Mapped[str] = mapped_column(sa.String(45), unique=True, nullable=False)
    formula_quimica: Mapped[str] = mapped_column(sa.String(45), unique=True, nullable=False)

    picoles: Mapped[List["Picole"]] = relationship(
        "Picole",
        secondary="aditivos_nutritivos_picole",
        back_populates="aditivos_nutritivos",
        lazy="selectin"
    )

    def __repr__(self) -> str:
        return f'<AditivoNutritivo: {self.nome}>'
    
    def __str__(self):
        return f"AditivoNutritivo: {self.nome}"
    
    