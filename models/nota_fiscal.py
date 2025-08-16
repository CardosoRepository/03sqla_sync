import sqlalchemy as sa
import sqlalchemy.orm as orm

from datetime import datetime
from typing import List

from models.model_base import ModelBase
from models.revendedor import Revendedor
from models.lote import Lote

# Nota Fiscal pode ter vários lotes
lotes_nota_fiscal = sa.Table(
    'lotes_nota_fiscal',
    ModelBase.metadata,
    sa.Column('id_nota_fiscal', sa.Integer, sa.ForeignKey('notas_fiscais.id')),
    sa.Column('id_lote', sa.Integer, sa.ForeignKey('lotes.id'))
)

class NotaFiscal(ModelBase):
    __tablename__ = 'notas_fiscais'
    
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)

    id_revendedor: int = sa.Column(sa.Integer, sa.ForeignKey('revendedores.id'))
    revendedor: Revendedor = orm.relationship('Revendedor', lazy='joined'),

    # Uma nota fiscal pode ter vários lotes e um lote está ligado a uma nota fiscal
    lotes: List[Lote] = orm.relationship('Lote', secondary=lotes_nota_fiscal, backref='lote', lazy='dynamic')

    valor: float = sa.Column(sa.DECIMAL(8, 2), nullable=False)
    numero_serie: str = sa.Column(sa.String(45), nullable=False)
    descricao: str = sa.Column(sa.String(200), nullable=False)

    def __repr__(self) -> int:
        return f'<NotaFiscal: {self.id}>'

    def __str__(self):
        return f"NotaFiscal: {self.id}"

