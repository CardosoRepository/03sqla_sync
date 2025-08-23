from typing import Optional

from conf.db_session import create_session

from models.revendedor import Revendedor
from models.picole import Picole

def deletar_picole(id_picole: int) -> None:
    with create_session() as session:
        picole: Optional[Picole] = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            session.delete(picole)
            session.commit()
        else:
            print(f"Não existe picolé com ID {id_picole}")

def deletar_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()

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

    # id_revendedor = 3
    # select_filtro_revendedor(id_revendedor=id_revendedor)
    # deletar_revendedor(id_revendedor=id_revendedor)
    # select_filtro_revendedor(id_revendedor=id_revendedor)