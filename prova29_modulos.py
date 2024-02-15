def adicionar(nome, descricao, prioridade, categoria):
    dic = {
        'nome' : nome,
        'descricao' : descricao,
        'prioridade' : prioridade,
        'categoria' : categoria,
        'concluida' : False
    }
    return dic

def listar(lista):
    if len(lista) == 0:
            print("Nenhuma tarefa cadastrada!", end="\n\n")
    else:
        tarefas_ordenadas = sorted(lista, key=lambda x: x['nome'])
        for dic in tarefas_ordenadas:
            print(f"Nome.......: {dic['nome']}")
            print(f"Descrição..: {dic['descricao']}")
            print(f"Prioridade.: {'Alta' if dic['prioridade'] == 'A' else ('Média' if dic['prioridade'] == 'M' else 'Baixa')}")
            print(f"Categoria..: {dic['categoria']}")
            print(f"Concluída..: {'Não' if dic['concluida'] == False else 'Sim'}")
            criar_separador(30)
        print()
        print("Tarefas ordenadas por nome listadas com sucesso!", end="\n\n")

def marcar_como_concluida(lista):
    if len(lista) == 0:
        print("Nenhuma tarefa cadastrada!", end="\n\n")
    else:
        tarefas_nao_concluidas = [tarefa for tarefa in lista if not tarefa['concluida']]
        if len(tarefas_nao_concluidas) == 0:
            print("Não há nenhuma tarefa a ser concluída!", end="\n\n")
        else:
            print("Lista das tarefas não concluídas:", end="\n\n")
            for i, tarefa in enumerate(tarefas_nao_concluidas, start=1):
                print(f"{i}. {tarefa['nome']}")
            print()
            controle = True
            while controle:
                try:
                    numero_tarefa = int(input("Escolha o número da tarefa que deseja marcar como concluída: "))
                    if 1 <= numero_tarefa <= len(tarefas_nao_concluidas):
                        controle = False
                    else:
                        print("Por favor, escolha um número válido!", end="\n\n")
                except ValueError:
                    print("Por favor, digite um número válido!", end="\n\n")
            nome_tarefa = tarefas_nao_concluidas[numero_tarefa - 1]['nome']
            for dic in lista:
                if dic['nome'] == nome_tarefa:
                    dic['concluida'] = True
            print()
            print(f"Tarefa: |{nome_tarefa}| marcada com sucesso como concluída!", end="\n\n")

def exibir_por_prioridade(lista):
    if len(lista) == 0:
        print("Nenhuma tarefa cadastrada!", end="\n\n")
    else:
        prioridade_map = {"A": 1, "M": 2, "B": 3}
        tarefas_ordenadas = sorted(lista, key=lambda x: prioridade_map[x['prioridade']])
        tarefas_agrupadas = {}
        for tarefa in tarefas_ordenadas:
            prioridade = tarefa['prioridade']
            if prioridade not in tarefas_agrupadas:
                tarefas_agrupadas[prioridade] = []
            tarefas_agrupadas[prioridade].append(tarefa)
        for prioridade, tarefas in tarefas_agrupadas.items():
            print(f"Prioridade: {'Alta' if prioridade == 'A' else ('Média' if prioridade == 'M' else 'Baixa')}")
            print()
            for tarefa in tarefas:
                print(f"Nome.......: {tarefa['nome']}")
                print(f"Descrição..: {tarefa['descricao']}")
                print(f"Categoria..: {tarefa['categoria']}")
                print(f"Concluída..: {'Não' if tarefa['concluida'] == False else 'Sim'}")
                print()
            criar_separador(30)
        print()
        print("Tarefas por prioridade listadas com sucesso!", end="\n\n")

def exibir_por_categoria(lista):
    if len(lista) == 0:
        print("Nenhuma tarefa cadastrada!", end="\n\n")
    else:
        tarefas_ordenadas = sorted(lista, key=lambda x: x['categoria'])
        tarefas_agrupadas = {}
        for tarefa in tarefas_ordenadas:
            categoria = tarefa['categoria']
            if categoria not in tarefas_agrupadas:
                tarefas_agrupadas[categoria] = []
            tarefas_agrupadas[categoria].append(tarefa)
        for categoria, tarefas in tarefas_agrupadas.items():
            print(f"Categoria: {categoria}")
            print()
            for tarefa in tarefas:
                print(f"Nome.......: {tarefa['nome']}")
                print(f"Descrição..: {tarefa['descricao']}")
                print(f"Prioridade.: {'Alta' if tarefa['prioridade'] == 'A' else ('Média' if tarefa['prioridade'] == 'M' else 'Baixa')}")
                print(f"Concluída..: {'Não' if tarefa['concluida'] == False else 'Sim'}")
                print()
            criar_separador(30)
        print()
        print("Tarefas por categoria listadas com sucesso!", end="\n\n")

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

# Função para validar prioridade:
def validar_prioridade(mensagem: str) -> str:
    Controle = True
    while Controle:
        resposta = input(mensagem).upper()
        if resposta == "A" or resposta == "M" or resposta == "B":
            Controle = False
            return resposta
        else:
            print("Valor inválido! Digite A, M ou B", end="\n\n")

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