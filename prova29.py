"""
[PY-A06] ENTREGUE SEU PROJETO ABAIXO SEGUINDO AS OBSERVAÇÕES

SUGESTÃO DE PROJETO: 

GERENCIADOR DE TAREFAS DIÁRIAS

Configuração do Ambiente Virtual:

Crie um ambiente virtual utilizando o módulo venv para isolar as dependências do projeto.
Definição de Dados:

Utilize estruturas de dados, como dicionários, para representar as tarefas. Cada tarefa deve conter informações como nome,
descrição, prioridade e categoria.

Funções:

Implemente funções para adicionar tarefas, listar tarefas, marcar tarefas como concluídas, exibir tarefas por prioridade ou
categoria, e outras funcionalidades desejadas.

Menu de Comandos:

Desenvolva um menu de comandos de linha de comando que permita ao usuário interagir com o programa. Este menu deve oferecer
opções para realizar operações como adicionar, listar, marcar como concluídas e visualizar tarefas por prioridade ou categoria.
O projeto será organizado em partes distintas, utilizando diversas estruturas de dados e funções para oferecer uma experiência
completa de gerenciamento de tarefas aos usuários.
"""
from prova29_modulos import *
 
# Iniciar sem cadastro
#tarefas = []

# Iniciar com tarefas já cadastradas
tarefas = [
    {"nome": "Comprar leite", "descricao": "Ir ao mercado e comprar leite", "prioridade": "A", "categoria": "Compras", "concluida": False},
    {"nome": "Estudar Python", "descricao": "Estudar programação em Python", "prioridade": "M", "categoria": "Estudos", "concluida": False},
    {"nome": "Fazer exercícios", "descricao": "Praticar exercícios físicos", "prioridade": "B", "categoria": "Saúde", "concluida": False},
    {"nome": "Ler livro", "descricao": "Ler o novo livro", "prioridade": "A", "categoria": "Lazer", "concluida": False},
    {"nome": "Fazer compras", "descricao": "Fazer compras no supermercado", "prioridade": "B", "categoria": "Compras", "concluida": False},
    {"nome": "Estudar Matemática", "descricao": "Estudar álgebra linear", "prioridade": "M", "categoria": "Estudos", "concluida": False}
]
limpar_tela()
controle_principal = True
while controle_principal:
    titulo_menu = "gerenciador de tarefas diárias"
    opcoes_menu = ["Adicionar tarefa", "Listar tarefas", "Marcar tarefa como concluída", "Exibir tarefas por prioridade",
                   "Exibir tarefas por categoria", "Encerrar aplicação"]
    escolha_usuario = criar_menu_tipo_1(titulo_menu, opcoes_menu)
    print()
    print(f"Você escolheu a opção {escolha_usuario}:", end="\n\n")
    criar_titulo(opcoes_menu[escolha_usuario - 1], 30)
    print()
    if escolha_usuario == 1:
        recebe_nome = validar_texto("Nome: ")
        print()
        recebe_descricao = validar_texto("Descrição: ")
        print()
        recebe_prioridade = validar_prioridade("Prioridade (A para alta - M para média - B para baixa): ")
        print()
        recebe_categoria = validar_texto("Categoria: ")
        print()
        tarefa = adicionar(recebe_nome, recebe_descricao, recebe_prioridade, recebe_categoria)
        tarefas.append(tarefa)
        print("Cadastro realizado com sucesso!", end="\n\n")
        pausar()
        limpar_tela()
    elif escolha_usuario == 2:
        listar(tarefas)
        pausar()
        limpar_tela()        
    elif escolha_usuario == 3:
        marcar_como_concluida(tarefas)
        pausar()
        limpar_tela()
    elif escolha_usuario == 4:
        exibir_por_prioridade(tarefas)
        pausar()
        limpar_tela()
    elif escolha_usuario == 5:
        exibir_por_categoria(tarefas)
        pausar()
        limpar_tela()        
    else:
        controle_principal = False
        print("Encerrando a aplicação.", end="\n\n")