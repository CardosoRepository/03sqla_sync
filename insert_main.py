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

def insert_aditivo_nutritivo() -> AditivoNutritivo:
    print("Cadastrando Aditivo Nutritivo...")

    nome: str = input("Informe o nome do Aditivo Nutritivo: ")
    formula_quimica: str = input("Informe a fórmula química do Aditivo Nutritivo: ")

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)
        session.commit()
        session.refresh(an)

        print("Aditivo Nutritivo cadastrado com sucesso!")
        print(f"ID: {an.id}")
        print(f"Data: {an.data_criacao}")
        print(f"Nome: {an.nome}")
        print(f"Fórmula Química: {an.formula_quimica}")

        return an

def insert_sabor() -> None:
    print("Inserindo sabor...")

    nome: str = input("Informe o nome do sabor: ")

    novo_sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(novo_sabor)
        session.commit()
        session.refresh(novo_sabor)

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
        session.refresh(novo_tipo_embalagem)

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
        session.refresh(novo_tipo_picole)

        print("Tipo de picolé cadastrado com sucesso!")
        print(f"ID: {novo_tipo_picole.id}")
        print(f"Nome: {novo_tipo_picole.nome}")

def insert_ingrediente() -> Ingrediente:
    print("Inserindo ingrediente...")

    nome: str = input("Informe o nome do ingrediente: ")

    novo_ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(novo_ingrediente)
        session.commit()
        session.refresh(novo_ingrediente)

        return novo_ingrediente

def insert_conservante() -> Conservante:
    print("Inserindo conservante...")

    nome: str = input("Informe o nome do conservante: ")
    descricao: str = input("Informe a descrição do conservante: ")

    novo_conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(novo_conservante)
        session.commit()
        session.refresh(novo_conservante)

        return novo_conservante
    
    # print("Conservante cadastrado com sucesso!")
    # print(f"ID: {novo_conservante.id}")
    # print(f"Nome: {novo_conservante.nome}")
    # print(f"Descrição: {novo_conservante.descricao}")

def insert_revendedor() -> Revendedor:
    print("Inserindo revendedor...")

    cnpj: str = input("Informe o cnpj do revendedor: ")
    razao_social: str = input("Informe a razão social do revendedor: ")
    contato: str = input("Informe o contato do revendedor: ")

    novo_revendedor: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(novo_revendedor)
        session.commit()
        session.refresh(novo_revendedor)

        return novo_revendedor

def insert_lote() -> Lote:
    print("Inserindo lote...")

    id_tipo_picole: int = input("Informe o ID do tipo de picolé: ")
    quantidade: int = input("Informe a quantidade do lote: ")

    novo_lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

    with create_session() as session:
        session.add(novo_lote)
        session.commit()
        session.refresh(novo_lote)

        return novo_lote

def insert_nota_fiscal() -> None:
    print("Inserindo nota fiscal...")

    valor: float = input("Informe o valor da nota fiscal: ")
    numero_serie: str = input("Informe o número de série da nota fiscal: ")
    descricao: str = input("Informe a descrição da nota fiscal: ")

    id_revendedor: int = insert_revendedor().id

    nova_nota_fiscal: NotaFiscal = NotaFiscal(valor=valor, numero_serie=numero_serie, descricao=descricao, id_revendedor=id_revendedor)

    lote1 = insert_lote()
    nova_nota_fiscal.lotes.append(lote1)

    with create_session() as session:
        session.add(nova_nota_fiscal)
        session.commit()
        session.refresh(nova_nota_fiscal)

        print(f"Nota fiscal cadastrada com sucesso!")
        print(f"ID: {nova_nota_fiscal.id}")
        print(f"Número de Série: {nova_nota_fiscal.numero_serie}")
        print(f"Descrição: {nova_nota_fiscal.descricao}")
        print(f"ID Revendedor: {nova_nota_fiscal.id_revendedor}")
        print(f"Revendedor: {nova_nota_fiscal.revendedor.razao_social}")

def insert_picole() -> None:
    print("Inserindo picolé...")

    preco: float = input("Informe o preço do picolé: ")

    id_sabor: int = input("Informe o ID do sabor: ")
    id_tipo_embalagem: int = input("Informe o ID do tipo da embalagem: ")
    id_tipo_picole: int = input("Informe o ID do tipo do picolé: ")

    novo_picole: Picole = Picole(
        preco=preco,
        id_sabor=id_sabor,
        id_tipo_embalagem=id_tipo_embalagem,
        id_tipo_picole=id_tipo_picole
    )

    ingrediente1 = insert_ingrediente()
    novo_picole.ingredientes.append(ingrediente1)

    ingrediente2 = insert_ingrediente()
    novo_picole.ingredientes.append(ingrediente2)

    conservante = insert_conservante()
    novo_picole.conservantes.append(conservante)

    aditivo_nutritivo = insert_aditivo_nutritivo()
    novo_picole.aditivos_nutritivos.append(aditivo_nutritivo)

    with create_session() as session:
        session.add(novo_picole)
        session.commit()
        session.refresh(novo_picole)

        print(f"Picolé cadastrado com sucesso!")
        print(f"ID: {novo_picole.id}")
        print(f"Preço: {novo_picole.preco}")
        print(f"Sabor: {novo_picole.sabor.nome}")
        print(f"Tipo Picolé: {novo_picole.tipo_picole.nome}")
        print(f"Tipo Embalagem: {novo_picole.tipo_embalagem.nome}")
        print(f"Ingredientes: {novo_picole.ingredientes}")
        print(f"Conservantes: {novo_picole.conservantes}")
        print(f"Aditivos Nutritivos: {novo_picole.aditivos_nutritivos}")

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

    # lote = insert_lote()
    # print(f'ID: {lote.id}')
    # print(f'ID Tipo Picolé: {lote.id_tipo_picole}')
    # print(f'Quantidade: {lote.quantidade}')

    # insert_nota_fiscal()

    insert_picole()

    print ('...')