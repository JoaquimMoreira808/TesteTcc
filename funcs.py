Orientadores = []

def cadastrar_orientador(nome: str):
    Orientador = {"nome": nome, "alunos": []}
    Orientadores.append(Orientador)
    print(f"Orientador {nome} cadastrado com sucesso!")

alunos = []

def cadastrar_aluno(nome: str, matricula: int, orientador: str):
    aluno = {"nome": nome, "matricula": matricula, "orientador": orientador, "entregas": []}
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")

def listar_orientadores():
    print("Lista de orientadores:")
    for o in Orientadores:
        print(f"- {o['nome']} (Alunos: {len(o['alunos'])})")

def listar_orientador(nome: str):
    for o in Orientadores:
        if o["nome"] == nome:
            print(f"Orientador: {o['nome']}")
            if o["alunos"]:
                print("Alunos orientados:")
                for aluno in o["alunos"]:
                    print(f"  - {aluno['nome']} (Matrícula: {aluno['matricula']})")
            else:
                print("Nenhum aluno cadastrado ainda.")
            return
    print(f"Orientador '{nome}' não encontrado.")

cadastrar_orientador("Marcelo")
cadastrar_orientador("Camila")
cadastrar_orientador("Joaquim")

cadastrar_aluno("Lucas", 12345, "Camila")
cadastrar_aluno("Isabela", 54321, "Joaquim")
cadastrar_aluno("Fernando", 67890, "Marcelo")
cadastrar_aluno("Ana", 99999, "Rosangela")
cadastrar_aluno("Rodrigo", 88888, "Camila")

print()
listar_orientadores()
print()

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

menu()

#parte feita em sala na quarta feira
Orientadores = []

def CadastrarOrientador():
    nome = input("Digite o nome do Ronaldo: ")
    Orientador = {"nome":nome, "Alunos": []}



Alunos = []
def CadastrarAlunos():
    nome = input("Digite o nome do aluno: ")
    matricula = int(input("Digite a matricula do aluno:"))
    orientador = input("Digite o nome do orientador: ")

    Aluno = {"nome":nome, "matricula":matricula, "orientador":orientador, "entregas": []}
    Alunos.append(Aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")

# Buscar Aluno
def BuscarAluno(matricula):
    for aluno in Alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None


CadastrarAlunos()

matricula_busca = int(input("Digite a matricula do aluno para buscar: "))
aluno_encontrado = BuscarAluno(matricula_busca)

if aluno_encontrado:
    print(f"Aluno encontrado: {aluno_encontrado}")
else:
    print("Aluno não encontrado:")



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


    
# Atribuição de notas
def atribuir_nota(nota:float, matricula:int):
    matricula = input("Digite a matricula do aluno: ")
    aluno = next((a for a in Alunos if a ["matricula"] == matricula), None)
    nota = input("Digite a nota do aluno: ")
