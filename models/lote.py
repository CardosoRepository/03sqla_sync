import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime

from models.model_base import ModelBase
from models.tipo_picole import TipoPicole

class Lote(ModelBase):
    __tablename__ = 'lotes'
    
    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now, index=True)

    id_tipo_picole: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey('tipos_picole.id'), nullable=False)
    tipo_picole: Mapped[TipoPicole] = relationship('TipoPicole', lazy='joined')

    quantidade: Mapped[int] = mapped_column(sa.Integer, nullable=False)

    def __repr__(self) -> int:
        return f'<Lote: {self.id}>'

    def __str__(self):
        return f"Lote: {self.id}"

