"""
[PY-A08] Você está desenvolvendo um programa para gerenciar uma lista de compras. O programa permite adicionar produtos à
lista, visualizar a lista de produtos, atualizar as informações de um produto existente e remover produtos da lista.
Além disso, o programa calcula o valor total de todos os produtos da lista.

O programa oferece as seguintes opções:

Adicionar produtos: O usuário pode adicionar um novo produto à lista informando o nome, a quantidade e o valor unitário do
produto. O programa calcula automaticamente o valor total do produto (quantidade * valor unitário) e atualiza o valor total
de todos os produtos.

Ver a lista de produtos: O programa exibe a lista de produtos adicionados até o momento, mostrando o nome do produto,
o valor unitário, a quantidade e o valor total do produto. Além disso, exibe o valor total de todos os produtos da lista.

Atualizar produtos: O usuário pode atualizar as informações de um produto existente na lista. O programa solicita o nome
do produto que deseja atualizar e, em seguida, permite editar o nome, a quantidade e o valor unitário do produto.
O programa recalcula automaticamente o valor total do produto e o valor total de todos os produtos.

Remover produto: O usuário pode remover um produto da lista informando o nome do produto que deseja remover.
O programa atualiza automaticamente o valor total de todos os produtos.

Encerrar programa: Encerra a execução do programa.

O programa utiliza uma lista para armazenar os produtos, onde cada produto é representado por um dicionário com as
informações: "produto", "valor", "quantidade" e "total". A variável totalProdutos é utilizada para armazenar o valor
total de todos os produtos da lista.

A cada operação realizada, o programa exibe mensagens indicando o resultado da operação.
"""
from prova14_modulos import *

limpar_tela()
produtos = []
valor_total_produtos = 0
controle_principal = True
while controle_principal:
    titulo_menu = "cadastro de produtos"
    opcoes_menu = ["Adicionar produtos", "Ver a lista de produtos", "Atualizar produtos", "Remover produto", "Encerrar programa"]
    escolha_usuario = criar_menu_tipo_1(titulo_menu, opcoes_menu)
    print()
    print(f"Você escolheu a opção {escolha_usuario}:", end="\n\n")
    criar_titulo(opcoes_menu[escolha_usuario - 1], 20)
    print()
    if escolha_usuario == 1:
        nome_produto = validar_texto("Nome do produto: ")
        print()
        valor_produto = validar_numero_somente_positivo_float("Valor do produto: R$ ")
        print()
        quant_produto = validar_numero_somente_positivo_int("Quantidade do produto: ")
        print()
        valor_total_produto = round(quant_produto * valor_produto, 2)
        produto = cadastrar_produto(nome_produto, valor_produto, quant_produto, valor_total_produto)
        produtos.append(produto)
        valor_total_produtos = calcula_valor_total_produtos(produtos, produto)
        print("Cadastro realizado com sucesso.")
        pausar()
        limpar_tela()
    if escolha_usuario == 2:
        listar_produtos(produtos, produto)
        print()
        criar_titulo("valor total de todos os produtos da lista:", 20)
        print()
        print(f"R$ {round(valor_total_produtos, 2):.2f}", end="\n\n")
        pausar()
        limpar_tela()
        
    if escolha_usuario == 3:
        busca_nome = validar_texto("Nome do produto para atualizar no cadastro: ")
        print()
        if buscar_produto(produtos, produto, busca_nome) == True:
            nome_produto = validar_texto("Novo nome do produto: ")
            print()
            valor_produto = validar_numero_somente_positivo_float("Novo valor do produto: R$ ")
            print()
            quant_produto = validar_numero_somente_positivo_int("Nova quantidade do produto: ")
            print()
            produto = atualizar_produto(produtos, produto, busca_nome, nome_produto, valor_produto, quant_produto)
            valor_total_produtos = calcula_valor_total_produtos(produtos, produto)
            print("Atualização realizada com sucesso.")
        else:
            print("Produto não encontrado.")
            print()
        pausar()
        limpar_tela()

    if escolha_usuario == 4:
        busca_nome = validar_texto("Nome do produto para remover do cadastro: ")
        print()
        if buscar_produto(produtos, produto, busca_nome) == True:
            remover_produto(produtos, produto, busca_nome)
            valor_total_produtos = calcula_valor_total_produtos(produtos, produto)
            print("Produto removido com sucesso.")
        else:
            print("Produto não encontrado.")
            print()
        pausar()
        limpar_tela()

    if escolha_usuario == 5:
        controle_principal = False
        print("Encerrando o programa.", end="\n\n")
        print()