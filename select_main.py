from typing import List, Optional

from sqlalchemy import func
from sqlalchemy.orm import configure_mappers

from conf.helpers import formata_data
from conf.db_session import create_session

import models.__all_models
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.revendedor import Revendedor
from models.picole import Picole
from models.nota_fiscal import NotaFiscal

configure_mappers()

def select_todos_aditivos_nutritivos() -> None:
    """
    Seleciona todos os aditivos nutritivos do banco de dados.
    """

    with create_session() as session:
        aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo).all()

    for an in aditivos_nutritivos:
        print(f'ID: {an.id}, Data: {formata_data(an.data_criacao)}, Nome: {an.nome}, Fórmula Química: {an.formula_quimica}')

def select_filtro_sabores(id_sabor: int) -> None:
    """Seleciona um sabor específico do banco de dados.

    Keyword arguments:
    id_sabor -- ID do sabor a ser selecionado
    Return: None
    """
    
    with create_session() as session:
        # Forma 1 -> Retorna None caso não encontre o sabor
        # sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).first()

        # Forma 2 -> Retorna None caso não encontre o sabor (Recomendado)
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        # Forma 3 -> exc.NoResultFound caso não encontre o sabor
        # sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one()

        # Forma 4 -> Usando where em vez de filter (one(), one_or_none(), first())
        # sabor: Sabor = session.query(Sabor).where(Sabor.id == id_sabor).one()

    if sabor:
        print(f'ID: {sabor.id}, Data: {formata_data(sabor.data_criacao)}, Nome: {sabor.nome}')
    else:
        print(f'Sabor com ID {id_sabor} não encontrado.')

def select_todos_sabores() -> None:
    """
    Seleciona todos os sabores do banco de dados.
    """

    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).all()

    for sabor in sabores:
        print(f'ID: {sabor.id}, Data: {formata_data(sabor.data_criacao)}, Nome: {sabor.nome}')

def select_picole() -> None:
    """
    Seleciona todos os picolés do banco de dados.
    """

    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).all()

    for picole in picoles:
        print(
            "ID:", picole.id, ",",
            "Data:", formata_data(picole.data_criacao), ",",
            "Preço:", picole.preco, ",",

            "ID Sabor:", picole.sabor.id if picole.sabor else "N/A", ",",
            "Sabor:", picole.sabor.nome if picole.sabor else "N/A", ",",

            "ID Embalagem:", picole.tipo_embalagem.id if picole.tipo_embalagem else "N/A", ",",
            "Embalagem:", picole.tipo_embalagem.nome if picole.tipo_embalagem else "N/A", ",",

            "ID Tipo Picolé:", picole.tipo_picole.id if picole.tipo_picole else "N/A", ",",
            "Tipo Picolé:", picole.tipo_picole.nome if picole.tipo_picole else "N/A"

            "Ingredientes:", picole.ingredientes if picole.ingredientes else "N/A", ",",
            "Aditivos Nutritivos:", picole.aditivos_nutritivos if picole.aditivos_nutritivos else "N/A", ",",
            "Conservantes:", picole.conservantes if picole.conservantes else "N/A"
        )

def select_order_by_sabor() -> None:
    """
    Seleciona todos os picolés ordenados por sabor.
    """

    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).order_by(Sabor.data_criacao.desc()).all()

    for sabor in sabores:
        print(f'ID: {sabor.id}')
        print(f'Nome: {sabor.nome}')

def select_group_by_picole() -> None:
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).group_by(Picole.id, Picole.id_tipo_picole).all()

    for picole in picoles:
        print(f'ID: {picole.id}')
        print(f'Tipo Picolé: {picole.tipo_picole}')
        print(f'Sabor: {picole.sabor}')
        print(f'Preço: {picole.preco}')

def select_limit() -> None:
    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).limit(25)

        for sabor in sabores:
            print(f"ID: {sabor.id}")
            print(f"Nome: {sabor.nome}")

def select_count_revendedor() -> None:
    with create_session() as session:
        qtd: int = session.query(Revendedor).count()
        print(f"Quantidade de Revendedores: {qtd}")

def select_count_agregacao() -> None:
    with create_session() as session:
        resultado: List = session.query(
            func.sum(Picole.preco).label("soma"),
            func.avg(Picole.preco).label("média"),
            func.min(Picole.preco).label("mais_barato"),
            func.max(Picole.preco).label("mais_caro"),
        ).all()

        print(f"Resultado: {resultado}")
        print (f"A soma de todos os picolés é: {resultado[0][0]}")
        print (f"A média de todos os picolés é: {resultado[0][1]}")
        print (f"O picolé mais barato é: {resultado[0][2]}")
        print (f"O picolé mais caro é: {resultado[0][3]}")

def select_filtro_picole(id_picole: int) -> None:
    """
    Seleciona um picolé específico do banco de dados.
    """
    
    with create_session() as session:
        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

    if picole:
        print(f'ID: {picole.id}, Data: {formata_data(picole.data_criacao)}, Sabor: {picole.sabor.nome}')
    else:
        print(f'Sabor com ID {id_picole} não encontrado.')

def select_todas_notas_fiscais() -> None:
    """
    Seleciona todas notas fiscais do banco de dados.
    """

    with create_session() as session:
        notas_fiscais: List[NotaFiscal] = session.query(NotaFiscal).order_by(NotaFiscal.id_revendedor).all()

    for nota_fiscal in notas_fiscais:
        print(f'ID: {nota_fiscal.id}, Data: {formata_data(nota_fiscal.data)}, Valor: {nota_fiscal.valor}, ID Revendedor: {nota_fiscal.id_revendedor}, Revendedor: {nota_fiscal.revendedor.razao_social}, Número de Série: {nota_fiscal.numero_serie}, Descrição: {nota_fiscal.descricao}')

def select_filtro_revendedor(id_revendedor: int) -> None:
    """
    Seleciona um revendedor específico do banco de dados.
    """

    with create_session() as session:
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()

    if revendedor:
        print(f'ID: {revendedor.id}, Razão Social: {revendedor.razao_social}')
    else:
        print(f'Revendedor com ID {id_revendedor} não encontrado.')


if __name__ == "__main__":
    # select_todos_aditivos_nutritivos()
    # select_todos_sabores()
    # select_filtro_sabores(1)
    # select_picole()
    # select_order_by_sabor()
    # select_group_by_picole()
    # select_limit()
    # select_count_revendedor()
    # select_count_agregacao()
    print ('---')