professores = []

def cadastrar_orientador(nome: str):
    professor = {"nome": nome, "alunos": []}
    professores.append(professor)
    print(f"Professor {nome} cadastrado com sucesso!")

alunos = []

def cadastrar_aluno(nome: str, matricula: int, orientador: str):
    aluno = {"nome": nome, "matricula": matricula, "orientador": orientador, "entregas": []}
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")

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
