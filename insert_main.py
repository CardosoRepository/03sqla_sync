from conf.db_session import create_session

from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor

def insert_aditivo_nutritivo() -> None:
    print("Cadastrando Aditivo Nutritivo...")

    nome: str = input("Informe o nome do Aditivo Nutritivo: ")
    formula_quimica: str = input("Informe a fórmula química do Aditivo Nutritivo: ")

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)
        session.commit()
    
    print("Aditivo Nutritivo cadastrado com sucesso!")
    print(f"ID: {an.id}")
    print(f"Data: {an.data_criacao}")
    print(f"Nome: {an.nome}")
    print(f"Fórmula Química: {an.formula_quimica}")

def insert_sabor() -> None:
    print("Inserindo sabor...")

    nome: str = input("Informe o nome do sabor: ")

    novo_sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(novo_sabor)
        session.commit()
    
    print("Sabor cadastrado com sucesso!")
    print(f"ID: {novo_sabor.id}")
    print(f"Nome: {novo_sabor.nome}")

def insert_tipo_embalagem() -> None:
    print("Inserindo tipo de embalagem...")

    nome: str = input("Informe o nome do tipo de embalagem: ")

    novo_tipo_embalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(novo_tipo_embalagem)
        session.commit()

    print("Tipo de embalagem cadastrado com sucesso!")
    print(f"ID: {novo_tipo_embalagem.id}")
    print(f"Nome: {novo_tipo_embalagem.nome}")

def insert_tipo_picole() -> None:
    print("Inserindo tipo de picolé...")

    nome: str = input("Informe o nome do tipo de picolé: ")

    novo_tipo_picole = TipoPicole(nome=nome)

    with create_session() as session:
        session.add(novo_tipo_picole)
        session.commit()

    print("Tipo de picolé cadastrado com sucesso!")
    print(f"ID: {novo_tipo_picole.id}")
    print(f"Nome: {novo_tipo_picole.nome}")

def insert_ingrediente() -> None:
    print("Inserindo ingrediente...")

    nome: str = input("Informe o nome do ingrediente: ")

    novo_ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(novo_ingrediente)
        session.commit()

    print("Ingrediente cadastrado com sucesso!")
    print(f"ID: {novo_ingrediente.id}")
    print(f"Nome: {novo_ingrediente.nome}")

def insert_conservante() -> None:
    print("Inserindo conservante...")

    nome: str = input("Informe o nome do conservante: ")
    descricao: str = input("Informe a descrição do conservante: ")

    novo_conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(novo_conservante)
        session.commit()

    print("Conservante cadastrado com sucesso!")
    print(f"ID: {novo_conservante.id}")
    print(f"Nome: {novo_conservante.nome}")
    print(f"Descrição: {novo_conservante.descricao}")

def insert_revendedor() -> Revendedor:
    print("Inserindo revendedor...")

    cnpj: str = input("Informe o cnpj do revendedor: ")
    razao_social: str = input("Informe a razão social do revendedor: ")
    contato: str = input("Informe o contato do revendedor: ")

    novo_revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(novo_revendedor)
        session.commit()

    return novo_revendedor

if __name__ == "__main__":
    # insert_aditivo_nutritivo()
    
    # insert_sabor()

    # insert_tipo_embalagem()

    # insert_tipo_picole()

    # insert_ingrediente()

    # insert_conservante()

    # rev = insert_revendedor()
    # print(f'ID: {rev.id}')
    # print(f'CNPJ: {rev.cnpj}')
    # print(f'Razão Social: {rev.razao_social}')
    # print(f'Contato: {rev.contato}')

    print ('...')