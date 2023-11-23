def calcula_valor_total_produtos(lista, dic):
    total = 0
    for dic in lista:
        total += dic['valor total do produto']
    return total

def cadastrar_produto(nome, valor_produto, quant_produto, valor_total_produto):
    dic = {
        'produto' : nome,
        'valor do produto' : valor_produto,
        'quant do produto' : quant_produto,
        'valor total do produto' : valor_total_produto
    }
    return dic

def listar_produtos(lista, dic):
    for dic in lista:
            print(f"Nome.......: {dic['produto']}")
            print(f"Valor......: R$ {dic['valor do produto']:.2f}")
            print(f"Quantidade.: {dic['quant do produto']}")
            print(f"Valor total: R$ {dic['valor total do produto']:.2f}")
            print()
            criar_separador(20)
            print()

def buscar_produto(lista, dic, nome):
    tem = 0
    for dic in lista:
        if dic['produto'] == nome:
            tem += 1
    if tem == 0:
        return False
    else:
        return True

def atualizar_produto(lista, dic, nome, nome_novo, valor_produto, quant_produto):
    for dic in lista:
        if dic['produto'] == nome:
            dic['produto'] = nome_novo
            dic['valor do produto'] = valor_produto
            dic['quant do produto'] = quant_produto
            valor_total_produto = round(quant_produto * valor_produto, 2)
            dic['valor total do produto'] = valor_total_produto
            break
    return dic

def remover_produto(lista, dic, nome):
    for dic in lista:
        if dic['produto'] == nome:
            lista.remove(dic)
            return

# Função para validar um campo string para não aceitar valor vazio:
def validar_texto(mensagem: str) -> str:
    Controle = True
    while Controle:
        texto = input(mensagem)
        if texto.strip() == "":
            print("O campo não pode ser vazio! Favor, digite um texto.", end="\n\n")
        else:
            Controle = False
            return texto

# Função para validar um numero int para não aceitar valor vazio, negativo e nem valor inválido:
def validar_numero_somente_positivo_int(mensagem: str) -> int:
    Controle = True
    while Controle:
        numero = input(mensagem)
        try:
            numero = int(numero)
            if numero >= 0:
                Controle = False
                return numero
            else:
                print("Valor inválido! Favor, digite um valor inteiro e não negativo.", end="\n\n")
        except ValueError:
            print("Valor inválido! Favor, digite um valor válido.", end="\n\n")

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

#Função para pausar a tela
def pausar():
    input("Pressione ENTER para continuar...")

#Função para limpar a tela
def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# tamanho_tamanho_referencia é o tamanho da string do menu principal criado nas funções criar_menu_tipo_1 e 2.
def criar_titulo(titulo: str, tamanho_referencia: int = 20):   
    if len(titulo) % 2 == 0:
        print("+","-"*(25-int((len(titulo)/2))+int(tamanho_referencia/2))," ",titulo.upper()," ","-"*(25-int((len(titulo)/2))+int(tamanho_referencia/2)+1),"+", sep="")
    else:
        print("+","-"*(25-int((len(titulo)/2))+int(tamanho_referencia/2))," ",titulo.upper()," ","-"*(25-int((len(titulo)/2))+int(tamanho_referencia/2)),"+", sep="")


# tamanho_tamanho_referencia é o tamanho da string do menu principal criado nas funções criar_menu_tipo_1 e 2.
def criar_separador(tamanho_referencia: int = 20):
    print("+","-"*(52+int(tamanho_referencia)),"+", sep="")

# Menu com o título dentro da borda:
def criar_menu_tipo_1(titulo, opcoes):
    # Imprime o título do menu
    print("+","-"*25," ",titulo.upper()," ","-"*25,"+", sep="")
       
    
    # Imprime as opções do menu
    for i, opcao in enumerate(opcoes, start=1):
        print(f"  {i}. {opcao}")
    print("+","-"*(52+len(titulo)),"+", sep="")
    print()

    # Solicita a escolha do usuário
    escolha = 0
    while escolha not in range(1, len(opcoes) + 1):
        try:
            escolha = int(input(f"Digite a opção desejada (1-{len(opcoes)}): "))
            if escolha not in range(1, len(opcoes) + 1):
                print("Por favor, insira uma opção válida.", end="\n\n")
        except ValueError:
            print("Por favor, insira um número válido.", end="\n\n")

    return escolha