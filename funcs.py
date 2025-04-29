Orientadores = []
Alunos = []

#================================================================================================

def cadastrar_orientador(nome: str):
    orientador = {"nome": nome, "alunos": []}
    Orientadores.append(orientador)
    print(f"Orientador {nome} cadastrado com sucesso")

#================================================================================================

def cadastrar_aluno(nome: str, matricula: int, orientador: str):
    if not any(o["nome"] == orientador for o in Orientadores):
        print(f"Erro: Orientador '{orientador}' não está cadastrado")
        return

    aluno = {"nome": nome, "matricula": matricula, "orientador": orientador, "entregas": []}
    Alunos.append(aluno)

    for o in Orientadores:
        if o["nome"] == orientador:
            o["alunos"].append(aluno)
            break

    print(f"Aluno {nome} cadastrado com sucesso")

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
                print("Nenhum aluno cadastrado aind")
            return
    print(f"Orientador '{nome}' não encontrado")

#================================================================================================

def BuscarAluno(matricula):
    for aluno in Alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None

#================================================================================================

def registrar_entrega():
    matricula = input("Digite a matrícula do aluno: ")
    if not matricula.isdigit():
        print("Matrícula invalida")
        return

    matricula = int(matricula)
    aluno = BuscarAluno(matricula)

    if not aluno:
        print("Aluno não encontrado")
        return

    for entrega in aluno["entregas"]:
        if entrega[2] is None:
            print("Tem um versão pendente de avaliação.")
            return

    versao_input = input("Digite o número da versão do TCC: ")
    if not versao_input.isdigit():
        print("Versão inválida.")
        return

    versao = int(versao_input)
    data = input("Digite a data de entrega (YYYY-MM-DD): ")

    aluno["entregas"].append((versao, data, None))
    print(f"Versão {versao} registrada com sucesso.")

#================================================================================================

def atribuir_nota():
    matricula = input("Digite a matrícula do aluno: ")
    if not matricula.isdigit():
        print("Matrícula inválida.")
        return

    matricula = int(matricula)
    aluno = BuscarAluno(matricula)

    if not aluno:
        print("Aluno não encontrado.")
        return

    for i, entrega in enumerate(aluno["entregas"]):
        if entrega[2] is None:
            nota_str = input("Digite a nota (0.0 a 10.0): ")
            ponto = nota_str.replace('.', '', 1)
            if not ponto.isdigit():
                print("Nota inválida.")
                return

            nota = float(nota_str)
            aluno["entregas"][i] = (entrega[0], entrega[1], nota)
            print(f"Nota {nota} atribuída a versão {entrega[0]}.")
            return

    print("Nenhuma entrega pendente para esse aluno.")

#================================================================================================

def listar_versoes_entregues(matricula):
    aluno = BuscarAluno(matricula)

    if not aluno:
        print("Aluno não encontrado.")
        return

    print(f"Versões entregues por {aluno['nome']}:")
    if aluno["entregas"]:
        for entrega in aluno["entregas"]:
            versao, data, nota = entrega
            status = f"Nota: {nota}" if nota is not None else "Aguardando avaliação"
            print(f"- Versão {versao}, Data: {data}, {status}")
    else:
        print("Nenhuma entrega registrada")

#================================================================================================

def listar_pendencias():
    encontrou = False
    for aluno in Alunos:
        for entrega in aluno["entregas"]:
            if entrega[2] is None:
                print(f"- {aluno['nome']} (Matrícula: {aluno['matricula']}), Versão {entrega[0]}, Entregue em: {entrega[1]}")
                encontrou = True
    if not encontrou:
        print("Nenhuma entrega pendente de avaliação")

#================================================================================================

def gerar_relatorio_orientador(nome):
    orientador = next((o for o in Orientadores if o["nome"] == nome), None)

    if not orientador:
        print("Orientador não encontrado")
        return

    print(f"Relatório de {orientador['nome']}:")
    alunos_do_orientador = [a for a in Alunos if a["orientador"] == nome]

    if not alunos_do_orientador:
        print("Nenhum aluno cadastrado")
        return

    soma_ultimas = 0
    qtd_ultimas = 0

    for aluno in alunos_do_orientador:
        print(f"Aluno: {aluno['nome']} (Matrícula: {aluno['matricula']})")
        notas = [e[2] for e in aluno["entregas"] if e[2] is not None]

        if notas:
            media = sum(notas) / len(notas)
            print(f"  - Média das notas: {media:.2f}")
            for entrega in reversed(aluno["entregas"]):
                if entrega[2] is not None:
                    soma_ultimas += entrega[2]
                    qtd_ultimas += 1
                    break
        else:
            print("  - Nenhuma nota registrada ainda")

        for entrega in aluno["entregas"]:
            versao, data, nota = entrega
            status = f"Nota: {nota}" if nota is not None else "Aguardando avaliação"
            print(f"  - Versão {versao}, Data: {data}, {status}")

    if qtd_ultimas > 0:
        media_geral = soma_ultimas / qtd_ultimas
        print(f"\nMédia geral (últimas versões avaliadas): {media_geral:.2f}")
    else:
        print("\nNenhuma nota atribuída ainda")

#================================================================================================

def menu():
    while True:
        print("""
=============================
    MENU DE CADASTROS
=============================
[1] Cadastrar Orientador
[2] Cadastrar Aluno
[3] Operações
[q] Sair
=============================
""")
        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Informe o nome do orientador: ")
            cadastrar_orientador(nome)

        elif opcao == "2":
            nome = input("Informe o nome do aluno: ")
            matricula = input("Informe a matrícula do aluno: ")
            if not matricula.isdigit():
                print("Matrícula inválida.")
                continue
            orientador = input("Informe o nome do orientador: ")
            cadastrar_aluno(nome, int(matricula), orientador)

        elif opcao == "3":
            menu_operacoes()

        elif opcao.lower() == "q":
            print("Encerrando programa!")
            break

        else:
            print("Digite uma opção válida!")

#================================================================================================

def menu_operacoes():
    while True:
        print("""
=============================
    MENU DE OPERAÇÕES
=============================
[1] Registrar nova entrega
[2] Registrar nota
[3] Listar alunos por orientador
[4] Listar versões entregues por aluno
[5] Listar pendências de avaliação
[6] Gerar relatório do orientador
[7] Listar orientadores
[8] Voltar ao menu principal              
=============================
""")
        opcao = input("Opção: ")

        if opcao == "1":
            registrar_entrega()

        elif opcao == "2":
            atribuir_nota()

        elif opcao == "3":
            nome = input("Informe o nome do orientador: ")
            listar_orientador(nome)

        elif opcao == "4":
            matricula = input("Informe a matrícula do aluno: ")
            if matricula.isdigit():
                listar_versoes_entregues(int(matricula))
            else:
                print("Matrícula inválida.")

        elif opcao == "5":
            listar_pendencias()

        elif opcao == "6":
            nome = input("Informe o nome do orientador: ")
            gerar_relatorio_orientador(nome)
        
        elif opcao == "7":
            listar_orientadores()

        elif opcao == "8": 
            break

        else:
            print("Digite uma opção válida!")

#================================================================================================

cadastrar_orientador("Marcelo")
cadastrar_orientador("Camila")
cadastrar_orientador("Joaquim")

cadastrar_aluno("Lucas", 12345, "Camila")
cadastrar_aluno("Isabela", 54321, "Joaquim")
cadastrar_aluno("Fernando", 67890, "Marcelo")
cadastrar_aluno("Ana", 99999, "Rosangela") 
cadastrar_aluno("Rodrigo", 88888, "Camila")

menu()
