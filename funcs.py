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
