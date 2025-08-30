from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship

from decimal import Decimal

from datetime import datetime

from models.revendedor import Revendedor
from models.lote import Lote

# colunas N:N com BigInteger e PK
class LotesNotaFiscal(SQLModel, table=True):
    id:             Optional[int] = Field(primary_key=True, autoincrement=True)
    id_nota_fiscal: Optional[int] = Field(default=None, foreign_key='notas_fiscais.id')
    id_lote:        Optional[int] = Field(default=None, foreign_key='lotes.id')


class NotaFiscal(SQLModel, table=True):
    __tablename__ = 'notas_fiscais'

    id:   Optional[int] = Field(primary_key=True, autoincrement=True)
    data: datetime      = Field(default=datetime.now, index=True)

    valor:        Decimal = Field(default=Decimal("0.00"), max_digits=8, decimal_places=2)
    numero_serie: str     = Field(max_length=45, unique=True)
    descricao:    str     = Field(max_length=200)

    id_revendedor: Optional[int] = Field(foreign_key='revendedores.id')
    revendedor:    Revendedor    = Relationship(
        "Revendedor", lazy='joined'
    )

    lotes: List[Lote] = Relationship(
        "Lote", link_model=LotesNotaFiscal, back_populates='lote', lazy='selectin'
    )

    def __repr__(self) -> str:
        return f'<NotaFiscal: {self.id}>'

