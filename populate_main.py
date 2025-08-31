import asyncio

import time

from tqdm import tqdm
from sqlalchemy.ext.asyncio import AsyncSession

from conf.helpers import gerar_string, gerar_int, gerar_float, gerar_cor
from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole


# 1) Aditivos Nutritivos
def populate_aditivo_nutritivo():
    print('Cadastrando Aditivo Nutritivo:')
    with create_session() as session:
        cor = gerar_cor()
        for _ in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            nome = gerar_string()
            formula_quimica = gerar_string(frase=True)
            session.add(AditivoNutritivo(nome=nome, formula_quimica=formula_quimica))
            time.sleep(0.05)
        session.commit()
    print('Aditivos Nutritivos cadastrados com sucesso')


# 2) Sabores
def populate_sabor():
    print('Cadastrando Sabores:')
    with create_session() as session:
        cor = gerar_cor()
        for _ in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            session.add(Sabor(nome=gerar_string()))
            time.sleep(0.05)
        session.commit()
    print('Sabores cadastrados com sucesso')


# 3) Tipos Embalagem
def populate_tipo_embalagem():
    print('Cadastrando Tipos Embalagem:')
    with create_session() as session:
        cor = gerar_cor()
        for _ in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            session.add(TipoEmbalagem(nome=gerar_string()))
            time.sleep(0.05)
        session.commit()
    print('Tipos Embalagem cadastrados com sucesso')


# 4) Tipos Picolé
def populate_tipo_picole():
    print('Cadastrando Tipos Picolé:')
    with create_session() as session:
        cor = gerar_cor()
        for _ in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            session.add(TipoPicole(nome=gerar_string()))
            time.sleep(0.05)
        session.commit()
    print('Tipos Picolé cadastrados com sucesso')


# 5) Ingredientes
def populate_ingrediente():
    print('Cadastrando Ingredientes:')
    with create_session() as session:
        cor = gerar_cor()
        for _ in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            session.add(Ingrediente(nome=gerar_string()))
            time.sleep(0.05)
        session.commit()
    print('Ingredientes cadastrados com sucesso')


# 6) Conservantes
def populate_conservante():
    print('Cadastrando Conservantes:')
    with create_session() as session:
        cor = gerar_cor()
        for _ in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            session.add(Conservante(nome=gerar_string(), descricao=gerar_string(frase=True)))
            time.sleep(0.05)
        session.commit()
    print('Conservantes cadastrados com sucesso')


# 7) Revendedor
def populate_revendedor():
    print('Cadastrando Revendedores:')
    with create_session() as session:
        cor = gerar_cor()
        for _ in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            session.add(Revendedor(
                cnpj=gerar_string(),
                razao_social=gerar_string(),
                contato=gerar_string()
            ))
            time.sleep(0.05)
        session.commit()
    print('Revendedores cadastrados com sucesso')


# 8) Lote
def populate_lote():
    print('Cadastrando Lotes:')
    with create_session() as session:
        cor = gerar_cor()
        for _ in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            id_tipo_picole = gerar_int()
            quantidade = gerar_int()
            session.add(Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade))
            time.sleep(0.05)
        session.commit()
    print('Lotes cadastrados com sucesso')


# 9) Nota Fiscal
def populate_nota_fiscal():
    print('Cadastrando Notas Fiscais:')
    with create_session() as session:
        cor = gerar_cor()
        for _ in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            valor = gerar_float(digitos=3)
            numero_serie = gerar_string()
            descricao = gerar_string(frase=True)
            id_revendedor = gerar_int()
            session.add(NotaFiscal(
                valor=valor,
                numero_serie=numero_serie,
                descricao=descricao,
                id_revendedor=id_revendedor
            ))
            time.sleep(0.05)
        session.commit()
    print('Notas Fiscais cadastradas com sucesso')


# 10) Picolé
def populate_picole():
    print('Cadastrando Picolés:')
    with create_session() as session:
        cor = gerar_cor()
        for _ in tqdm(range(1, 101), desc='Cadastrando...', colour=cor):
            preco = gerar_float()
            id_sabor = gerar_int()
            id_tipo_embalagem = gerar_int()
            id_tipo_picole = gerar_int()

            picole = Picole(
                preco=preco,
                id_sabor=id_sabor,
                id_tipo_embalagem=id_tipo_embalagem,
                id_tipo_picole=id_tipo_picole
            )

            # Ingredientes
            for _ in range(5):
                picole.ingredientes.append(Ingrediente(nome=gerar_string()))

            # Aditivos Nutritivos OU Conservantes
            op = gerar_float()
            if op > 5:
                for _ in range(3):
                    picole.aditivos_nutritivos.append(
                        AditivoNutritivo(nome=gerar_string(), formula_quimica=gerar_string(frase=True))
                    )
            else:
                for _ in range(3):
                    picole.conservantes.append(
                        Conservante(nome=gerar_string(), descricao=gerar_string(frase=True))
                    )

            session.add(picole)
            time.sleep(0.05)

        session.commit()
    print('Picolés cadastrados com sucesso')


def popular():
    # 1) Aditivos Nutritivos
    populate_aditivo_nutritivo()

    # 2) Sabores
    populate_sabor()

    # 3) Tipos Embalagem
    populate_tipo_embalagem()

    # 4) Tipos Picolé
    populate_tipo_picole()

    # 5) Ingredientes
    populate_ingrediente()

    # 6) Conservantes (deixe comentado se quiser verificar tabelas vazias)
    # populate_conservante()

    # 7) Revendedores
    populate_revendedor()

    # 8) Lotes
    populate_lote()

    # 9) Notas Fiscais
    populate_nota_fiscal()

    # 10) Picolé
    populate_picole()


if __name__ == '__main__':
    popular()