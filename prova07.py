"""
[PY-A04] Desenvolva um programa em Python que permita ao usuário digitar várias notas. Em seguida, crie uma função
chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno. Também crie uma função chamada
"verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média for menor
que 7, "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.
"""
def calcular_media(notas):
    total = 0
    media = 0
    for nota in notas:
        total += nota
    media = round(total / len(notas),2)
    return media

def verificar_situacao(media):
    if media == 10:
        situacao = "Parabéns, sua média é 10!"
    elif media < 7:
        situacao = "Reprovado"
    elif media >= 7:
        situacao = "Aprovado"
    return situacao

ListaDeNotas = []
Controle = True
while Controle:
    RecebeNota = float(input("Digite uma nota (digite -1 para encerrar.): "))
    if RecebeNota == -1:
        Controle = False
    else:
        ListaDeNotas.append(RecebeNota)
Media = calcular_media(ListaDeNotas)
Situacao = verificar_situacao(Media)
print(" ")
print("A média das notas do aluno é:", Media)
print("A situação do aluno é:", Situacao)