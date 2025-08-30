from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship

from decimal import Decimal

from datetime import datetime

from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.aditivo_nutritivo import AditivoNutritivo

# ---------- Tabelas de associação (N:N) ----------
class IngredientesPicole(SQLModel, table=True):
    id:             Optional[int] = Field(primary_key=True, autoincrement=True)
    id_picole:      Optional[int] = Field(foreign_key='picoles.id')
    id_ingrediente: Optional[int] = Field(foreign_key='ingredientes.id')


class ConservantesPicole(SQLModel, table=True):
    id:             Optional[int] = Field(primary_key=True, autoincrement=True)
    id_picole:      Optional[int] = Field(foreign_key='picoles.id')
    id_conservante: Optional[int] = Field(foreign_key='conservantes.id')

class AditivosNutritivosPicole(SQLModel, table=True):
    id:                   Optional[int] = Field(primary_key=True, autoincrement=True)
    id_picole:            Optional[int] = Field(foreign_key='picoles.id')
    id_aditivo_nutritivo: Optional[int] = Field(foreign_key='aditivos_nutritivos.id')

# -------------------- Model ----------------------
class Picole(SQLModel, table=True):
    __tablename__ = 'picoles'

    id:           Optional[int] = Field(primary_key=True, autoincrement=True)
    data_criacao: datetime      = Field(default=datetime.now, index=True)
    preco:        Decimal       = Field(default=Decimal("0.00"), max_digits=8, decimal_places=2)

    # FK + relacionamentos 1:N (cada picolé tem 1 sabor / tipo / embalagem)
    id_sabor: int   = Field(foreign_key='sabores.id')
    sabor:    Sabor = Relationship(lazy='joined')

    id_tipo_embalagem: int           = Field(foreign_key='tipos_embalagem.id')
    tipo_embalagem:    TipoEmbalagem = Relationship(lazy='joined')

    id_tipo_picole: int        = Field(foreign_key='tipos_picole.id')
    tipo_picole:    TipoPicole = Relationship(lazy='joined')

    # N:N
    ingredientes: List[Ingrediente] = Relationship(
        link_model=IngredientesPicole, 
        back_populates='ingrediente', 
        lazy='joined'
    )

    conservantes: List[Conservante] = Relationship(
        link_model=ConservantesPicole, 
        back_populates='conservante', 
        lazy='joined'
    )

    aditivos_nutritivos: List[AditivoNutritivo] = Relationship( 
        link_model=AditivosNutritivosPicole, 
        back_populates='aditivo_nutritivo', 
        lazy='joined'
    )

    def __repr__(self) -> str:
        return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}>'

