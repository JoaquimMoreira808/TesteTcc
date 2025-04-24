Professores = []

def cadastrar_professor(nome:str):
    Professor = {"nome":nome, "alunos": []}
    Professores.append(Professor)
    print(f"Professor {nome} cadastrado com sucesso!")

cadastrar_professor("Joaquim")

Alunos = []
def CadastrarAlunos(nome:str, matricula:int,orientador:str):
    Aluno = {"nome":nome, "matricula":matricula, "orientador":orientador, "entregas": []}
    Alunos.append(Aluno)
    print(f"Professor {nome} cadastrado com sucesso!")



