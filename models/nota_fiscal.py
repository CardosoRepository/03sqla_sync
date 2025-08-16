import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
from typing import List

from models.model_base import ModelBase
from models.revendedor import Revendedor
from models.lote import Lote

# colunas N:N com BigInteger e PK
lotes_nota_fiscal = sa.Table(
    'lotes_nota_fiscal',
    ModelBase.metadata,
    sa.Column('id_nota_fiscal', sa.BigInteger, sa.ForeignKey('notas_fiscais.id'), primary_key=True),
    sa.Column('id_lote', sa.BigInteger, sa.ForeignKey('lotes.id'), primary_key=True)
)

class NotaFiscal(ModelBase):
    __tablename__ = 'notas_fiscais'

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now, index=True)

    id_revendedor: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey('revendedores.id'), nullable=False)
    revendedor: Mapped[Revendedor] = relationship(
        back_populates='notas_fiscais', lazy='joined'
    )

    # Uma nota fiscal pode ter vários lotes e um lote está ligado a uma nota fiscal
    lotes: Mapped[List[Lote]] = relationship(
        'Lote', 
        secondary=lotes_nota_fiscal, 
        back_populates='notas_fiscais', 
        lazy='selectin'
    )

    valor: Mapped[float] = mapped_column(sa.DECIMAL(8, 2), nullable=False)
    numero_serie: Mapped[str] = mapped_column(sa.String(45), nullable=False)
    descricao: Mapped[str] = mapped_column(sa.String(200), nullable=False)

    def __repr__(self) -> int:
        return f'<NotaFiscal: {self.id}>'

    def __str__(self):
        return f"NotaFiscal: {self.id}"

