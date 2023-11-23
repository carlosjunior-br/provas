# [PY-A07] Você foi contratado para desenvolver um programa que calcule a média das notas de cada aluno de uma turma.
# Para isso, você deverá criar uma lista com as notas de cada aluno e, em seguida, implementar uma função que calcule a
# média aritmética das notas. Além disso, você deverá utilizar um loop while para pedir ao usuário que insira as notas dos
# alunos até que ele decida parar. Por fim, você deverá utilizar um loop for para imprimir a média de cada aluno.


# a) Escreva o código para a função que calcule a média aritmética das notas.
def media(notas):
    media = sum(notas) / len(notas)
    return media
#------------------------------------------------------------------------------------------


#Função para pausar a tela
def pausar():
    input("Pressione ENTER para encerrar...")

#Função para limpar a tela
def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para validar um campo string para aceitar somente S ou N:
def validar_sim_nao(mensagem: str) -> str:
    Controle = True
    while Controle:
        resposta = input(mensagem).upper()
        if resposta == "S" or resposta == "N":
            Controle = False
            return resposta
        else:
            print("Valor inválido! Digite S ou N.", end="\n\n")

# Função para validar um numero float para não aceitar valor vazio, negativo e nem valor inválido:
def validar_numero_somente_positivo_float(mensagem: str) -> float:
    Controle = True
    while Controle:
        numero = input(mensagem)
        try:
            numero = float(numero)
            if numero >= 0:
                Controle = False
                return numero
            else:
                print("Valor inválido! Favor, digite um valor decimal e não negativo.", end="\n\n")
        except ValueError:
            print("Valor inválido! Favor, digite um valor válido.", end="\n\n")

limpar_tela()
alunos = {}
controle = True
while controle:
    recebe_nome = input("Digite o nome do aluno: ")
    print()
    print("+----------Cadastre agora as notas deste aluno!----------+", end="\n\n")
# b) Escreva o código para o loop while que pede ao usuário que insira as notas dos alunos.
    notas = []
    controle_notas = True
    while controle_notas:
        recebe_nota = validar_numero_somente_positivo_float("Digite uma nota: ")
        notas.append(recebe_nota)
        print()
        opcao = validar_sim_nao("Deseja continuar cadastrando notas? (S/N): ")
        print()
        if opcao.upper() == "N":
            controle_notas = False
    alunos[recebe_nome] = {
        "notas" : notas
    }
#------------------------------------------------------------------------------------------
    opcao2 = validar_sim_nao("Deseja continuar cadastrando alunos? (S/N): ")
    print()
    if opcao2.upper() == "N":
            controle = False
    limpar_tela()
# c) Escreva o código para o loop for que imprime a média de cada aluno.
print("+---------- Lista dos alunos com suas respectivas médias ----------+", end="\n\n")
for aluno, dados in alunos.items():
    print()
    print("Nome......: ", aluno)
    print("Média.....: ", round(media(dados["notas"]),2))
    print("------------------------------", end="\n\n")
pausar()
print("Encerrando o programa.", end="\n\n")