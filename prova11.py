"""
Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos onde a chave deste dicionário
é o número de matrícula dos próprios alunos. O programa deve permitir adicionar, remover, atualizar e listar os alunos.
Para isso, você deve implementar um módulo que contém as seguintes funções:

AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário de alunos.

RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos.

AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno no dicionário .

VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um.

Lembre Se de Modularizar o código
"""
def pausar():
    input("Pressione ENTER para continuar...")

def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

from prova11_modulos import *

alunos = {}
controle = True
limpar_tela()

while controle:
    print("-"*25,"Menu","-"*25, end="\n\n")
    print("1 - Adicionar Aluno")
    print("2 - Remover Aluno")
    print("3 - Atualizar Aluno")
    print("4 - Listar Alunos")
    print("5 - Sair", end="\n\n")
    opcao = int(input("Digite a opção desejada: "))
    print()
    if opcao == 1:
        print("Você selecionou: Adicionar Aluno", end="\n\n")
        AdicionarAluno(alunos)
    if opcao == 2:
        print("Você selecionou: Remover Aluno", end="\n\n")
        RemoverAluno(alunos)
    if opcao == 3:
        print("Você selecionou: Atualizar Aluno", end="\n\n")
        AtualizarAluno(alunos)
    if opcao == 4:
        print("Você selecionou: Listar Alunos", end="\n\n")
        VerAlunos(alunos)
    if opcao == 5:
        print("Você selecionou: Sair", end="\n\n")
        controle = False
        print("Saindo")
    pausar()
    limpar_tela()