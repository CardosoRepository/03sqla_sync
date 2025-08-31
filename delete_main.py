from typing import Optional

from conf.db_session import create_session

from sqlmodel import select

from models.revendedor import Revendedor
from models.picole import Picole

def deletar_picole(id_picole: int) -> None:
    with create_session() as session:
        picole: Optional[Picole] = session.get(Picole, id_picole)

        if picole:
            session.delete(picole)
            session.commit()
        else:
            print(f"Não existe picolé com ID {id_picole}")

def deletar_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.get(Revendedor, id_revendedor)

        if revendedor:
            session.delete(revendedor)
            session.commit()
        else:
            print(f"Não existe revendedor com ID {id_revendedor}")

if __name__ == "__main__":
    from select_main import select_filtro_picole, select_todas_notas_fiscais, select_filtro_revendedor

    # id_picole = 21
    # select_filtro_picole(id_picole=id_picole)
    # deletar_picole(id_picole=id_picole)
    # select_filtro_picole(id_picole=id_picole)

    # id_revendedor = 4
    # select_filtro_revendedor(id_revendedor=id_revendedor)
    # deletar_revendedor(id_revendedor=id_revendedor)
    # select_filtro_revendedor(id_revendedor=id_revendedor)