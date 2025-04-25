#================================================================================================

Orientadores = [] # Array pra armazenar professores(Dicts)
Alunos = [] # Array pra armazenar alunos(Dicts)

#================================================================================================

def cadastrar_orientador(nome: str):
    Orientador = {"nome": nome, "alunos": []}
    Orientadores.append(Orientador)
    print(f"Orientador {nome} cadastrado com sucesso!")

#================================================================================================

def cadastrar_aluno(nome: str, matricula: int, orientador: str):
    aluno = {"nome": nome, "matricula": matricula, "orientador": orientador, "entregas": []}
    Alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")

#================================================================================================

def listar_orientadores():
    print("Lista de orientadores:")
    for orientador in Orientadores:
        print(f"- {orientador['nome']} (Alunos: {len(orientador['alunos'])})")

#================================================================================================

def listar_orientador(nome: str):
    for orientador in Orientadores:
        if orientador["nome"] == nome:
            print(f"Orientador: {orientador['nome']}")
            if orientador["alunos"]:
                print("Alunos orientados:")
                for aluno in orientador["alunos"]:
                    print(f"  - {aluno['nome']} (Matrícula: {aluno['matricula']})")
            else:
                print("Nenhum aluno cadastrado ainda.")
            return
    print(f"Orientador '{nome}' não encontrado.")

#================================================================================================

cadastrar_orientador("Marcelo")
cadastrar_orientador("Camila")
cadastrar_orientador("Joaquim")

cadastrar_aluno("Lucas", 12345, "Camila")
cadastrar_aluno("Isabela", 54321, "Joaquim")
cadastrar_aluno("Fernando", 67890, "Marcelo")
cadastrar_aluno("Ana", 99999, "Rosangela")
cadastrar_aluno("Rodrigo", 88888, "Camila")

#================================================================================================

# Buscar Aluno
def BuscarAluno(matricula):
    for aluno in Alunos:
        if aluno["matricula"]:
            return aluno
    return None

#================================================================================================

# Registrar Entrega de versão do TCC
def registrar_entrega():
    matricula = input("Digite a matricula do aluno: ")
    aluno = next((a for a in Alunos if a ["matricula"] == matricula), None)

    if not aluno:
        print("aluno não encontrado")
        return
    
    if any(entrega[2] is None for entrega in aluno["entregas"]):
        print("Você tem uma versão pendente de avaliação e não pode registrar uma nova entrega.")
        return
    
    versao = int(input("Digite o número da versão do TCC: "))
    data = input("Digite a data de entrega (formato YYYY-MM-DD): ")

    aluno["entregas"].append((versao, data, None))
    print(f"Versão {versao} do TCC registrada com sucesso.")

    registrar_entrega()

#================================================================================================
    
def atribuir_nota(nota:float, matricula:int):
    matricula = input("Digite a matricula do aluno: ")
    aluno = next((aluno for aluno in Alunos if aluno ["matricula"] == matricula), None)
    nota = input("Digite a nota do aluno: ")

#================================================================================================

def menu():
    print("""
=============================
    MENU DE CADASTROS
=============================
[1] Cadastrar Orientador
[2] Cadastrar Aluno
=============================
""")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Informe o nome do orientador: ")
        cadastrar_orientador(nome)
    
    else:
        print("Opção inválida.")

#================================================================================================
