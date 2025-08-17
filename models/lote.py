import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
from typing import List

from models.model_base import ModelBase

class Lote(ModelBase):
    __tablename__ = 'lotes'
    
    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now, index=True)

    id_tipo_picole: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey('tipos_picole.id'), nullable=False)
    tipo_picole: Mapped["TipoPicole"] = relationship('TipoPicole', lazy='joined')

    quantidade: Mapped[int] = mapped_column(sa.Integer, nullable=False)

    notas_fiscais: Mapped[List["NotaFiscal"]] = relationship(
        "NotaFiscal",
        secondary="lotes_nota_fiscal",
        back_populates="lotes",
        lazy="selectin"
    )

    def __repr__(self) -> str:
        return f'<Lote: {self.id}>'

    def __str__(self):
        return f"Lote: {self.id}"

