import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
from typing import List, Optional

from models.model_base import ModelBase
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.aditivo_nutritivo import AditivoNutritivo

# ---------- Tabelas de associação (N:N) ----------
ingredientes_picole = sa.Table(
    'ingredientes_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.BigInteger, sa.ForeignKey('picoles.id')),
    sa.Column('id_ingrediente', sa.BigInteger, sa.ForeignKey('ingredientes.id'))
)

conservantes_picole = sa.Table(
    'conservantes_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.BigInteger, sa.ForeignKey('picoles.id')),
    sa.Column('id_conservante', sa.BigInteger, sa.ForeignKey('conservantes.id'))
)

aditivos_nutritivos_picole = sa.Table(
    'aditivos_nutritivos_picole',
    ModelBase.metadata,
    sa.Column('id_picole', sa.BigInteger, sa.ForeignKey('picoles.id')),
    sa.Column('id_aditivo_nutritivo', sa.BigInteger, sa.ForeignKey('aditivos_nutritivos.id'))
)

# -------------------- Model ----------------------
class Picole(ModelBase):
    __tablename__ = 'picoles'

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now, index=True)
    preco: float = sa.Column(sa.DECIMAL(8, 2), nullable=False)

    # FK + relacionamentos 1:N (cada picolé tem 1 sabor / tipo / embalagem)
    id_sabor: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey('sabores.id'), nullable=False)
    sabor: Mapped[Sabor] = relationship(back_populates='picoles', lazy='joined')

    id_tipo_embalagem: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey('tipos_embalagem.id'), nullable=False)
    tipo_embalagem: Mapped[TipoEmbalagem] = relationship(back_populates='picoles', lazy='joined')

    id_tipo_picole: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey('tipos_picole.id'), nullable=False)
    tipo_picole: Mapped[TipoPicole] = relationship(back_populates='picoles', lazy='joined')

    # N:N
    ingredientes: Mapped[List[Ingrediente]] = relationship(
        'Ingrediente', 
        secondary=ingredientes_picole, 
        back_populates='picoles', 
        lazy='joined'
    )

    conservantes: Mapped[List[Conservante]] = relationship(
        'Conservante', 
        secondary=conservantes_picole, 
        back_populates='picoles', 
        lazy='joined'
    )

    aditivos_nutritivos: Mapped[List[AditivoNutritivo]] = relationship(
        'AditivoNutritivo', 
        secondary=aditivos_nutritivos_picole, 
        back_populates='picoles', 
        lazy='joined'
    )

    def __repr__(self) -> str:
        return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}>'

    def __str__(self):
        return f"Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}>"

