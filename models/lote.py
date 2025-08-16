import sqlalchemy as sa
import sqlalchemy.orm as orm

from datetime import datetime

from models.model_base import ModelBase
from models.tipo_picole import TipoPicole

class Lote(ModelBase):
    __tablename__ = 'lotes'
    
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)

    id_tipo_picole: int = sa.Column(sa.BigInteger, sa.ForeignKey('tipos_picole.id'), nullable=False)
    tipo_picole: TipoPicole = orm.relationship('TipoPicole', lazy='joined')

    quantidade: int = sa.Column(sa.Integer, nullable=False)

    def __repr__(self) -> int:
        return f'<Lote: {self.id}>'

    def __str__(self):
        return f"Lote: {self.id}"

