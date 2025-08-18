from conf.db_session import create_session

from models.sabor import Sabor
from models.picole import Picole

def atualizar_sabor(id_sabor: int, novo_nome: str) -> None:
    with create_session() as session:
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        if sabor:
            sabor.nome = novo_nome
            session.commit()
        else:
            print(f"Não existe sabor com ID {id_sabor}")

def atualizar_picole(id_picole: int, novo_preco: float, novo_sabor: int) -> None:
    with create_session() as session:
        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            picole.preco = novo_preco
            
            if novo_sabor:
                picole.id_sabor = novo_sabor

            session.commit()
        else:
            print(f"Não existe picolé com ID {id_picole}")

if __name__ == "__main__":
    # from select_main import select_filtro_sabores
    # id_sabor = 42

    # select_filtro_sabores(id_sabor=id_sabor)
    # atualizar_sabor(id_sabor=id_sabor, novo_nome='Morango')
    # select_filtro_sabores(id_sabor=id_sabor)

    from select_main import select_filtro_picole
    id_picole = 1
    novo_preco = 9.99
    id_novo_sabor = 1

    select_filtro_picole(id_picole=id_picole)
    atualizar_picole(id_picole=id_picole, novo_preco=novo_preco, novo_sabor=id_novo_sabor)
    select_filtro_picole(id_picole=id_picole)