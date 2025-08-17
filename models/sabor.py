import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
from typing import List

from models.model_base import ModelBase

class Sabor(ModelBase):
    __tablename__ = 'sabores'

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now, index=True)
    nome: Mapped[str] = mapped_column(sa.String(45), unique=True, nullable=False)

    picoles: Mapped[List["Picole"]] = relationship(
        "Picole",
        back_populates="sabor",
        lazy="selectin"
    )

    def __repr__(self) -> str:
        return f'<Sabor: {self.nome}>'

    def __str__(self):
        return f"Sabor: {self.nome}"

