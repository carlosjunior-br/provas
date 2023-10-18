"""
[PY-A03] Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando
um dicionário.

O programa deve fornecer as seguintes funcionalidades:

Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.

Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.

Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos
números de matrícula.

O programa deve ser executado em um loop contínuo até que o usuário escolha sair.
"""
Alunos = {}
Controle = True
while Controle:
    print("---------MENU DE OPÇÕE---------", end="\n\n")
    print("1 - Adicionar um aluno")
    print("2 - Remover um aluno")
    print("3 - Visualizar todos os alunos")
    print("0 - Sair", end="\n\n")
    RecebeOpcao = int(input("Digite o número correspondente da opção desejada: "))
    print(" ")
    if RecebeOpcao == 0:
        print("Saindo")
        Controle = False
    elif RecebeOpcao == 1:
        RecebeNome = input("Digite o nome do aluno: ")
        RecebeMatricula = int(input("Digite o número da matrícula do aluno: "))
        Alunos[RecebeMatricula] = RecebeNome
        print("Aluno cadastrado com sucesso!")
    elif RecebeOpcao == 2:
        RecebeMatricula = int(input("Digite o número da matrícula do aluno a ser excluído: "))
        if RecebeMatricula in Alunos:
            del Alunos[RecebeMatricula]
            print("Aluno excluído com sucesso!")
        else:
            print("Matrícula não encontrada.")
    elif RecebeOpcao == 3:
        print("Lista de todos os alunos:", end="\n\n")
        for Matricula, Nome in Alunos.items():
            print(f"Nome: {Nome}. Número da matrícula: {Matricula}.")
    else:
        print("Opção inválida.")