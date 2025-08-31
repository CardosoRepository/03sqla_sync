from pathlib import Path
from typing import Optional

from sqlalchemy.future.engine import Engine

from sqlmodel import Session, create_engine as _create_engine, SQLModel

__engine: Optional[Engine] = None

def create_engine(sqlite: bool = False) -> Engine:
    """
    Função para configuar conexão ao banco de dados.
    """
    
    global __engine

    if __engine:
        return __engine
    
    if sqlite:
        arquivo_db = 'db/picoles.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)

        conn_str = f'sqlite:///{arquivo_db}'
        __engine = _create_engine(url=conn_str, echo=False, connect_args={"check_same_thread": False})
    
    else:
        conn_str = "postgresql+psycopg://sql_alchemy:postgres@localhost:5433/picoles"
        __engine = _create_engine(url=conn_str, echo=False)

    return __engine

def create_session() -> Session:
    """
    Função para criar a seção de conexão ao banco de dados.
    """

    global __engine

    if not __engine:
        create_engine()

    session: Session = Session(__engine)

    return session

def create_tables() -> None:
    """
    Função para criar as tabelas no banco de dados.
    """
    
    global __engine

    if not __engine:
        create_engine()

    import models.__all_models

    with __engine.begin() as conn:
        conn.exec_driver_sql("DROP SCHEMA IF EXISTS public CASCADE;")
        conn.exec_driver_sql("CREATE SCHEMA public;")
        conn.exec_driver_sql("SET search_path TO public;")

    SQLModel.metadata.create_all(__engine)