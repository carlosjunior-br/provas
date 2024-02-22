import sqlite3
import os

#Função para pausar a tela
def pausar():
    input("Pressione ENTER para continuar...")

#Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class Clientes:
    def __init__(self, id_cliente: int, nome: str, email: str, data_cadastro: str, status: bool):
        self.id_cliente = id_cliente
        self.nome = nome
        self.email = email
        self.data_cadastro = data_cadastro
        self.status = status

class BancoDeDados:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
        self.conexao = None
        self.cursor = None

    def conectar(self):
        self.conexao = sqlite3.connect(self.nome_banco)
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        if self.conexao:
            self.conexao.close()

    def criar_tabela(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                                id_cliente INTEGER PRIMARY KEY,
                                nome TEXT NOT NULL,
                                email TEXT NOT NULL,
                                data_cadastro DATE NOT NULL,
                                status BOOL NOT NULL)''')
        self.conexao.commit()

    def inserir_cliente(self, nome: str, email: str, data_cadastro: str, status: bool):
        self.cursor.execute('''INSERT INTO Clientes (nome, email, data_cadastro, status)
                            VALUES (?, ?, ?, ?)''', (nome, email, data_cadastro, status))
        self.conexao.commit()

    def selecionar_clientes(self):
        self.cursor.execute('''SELECT * FROM Clientes''')
        clientes = self.cursor.fetchall()
        return [Clientes(*cliente) for cliente in clientes]
    
    def selecionar_clientes_ativos(self):
        self.cursor.execute('''SELECT * FROM Clientes WHERE status = ?''', (1,))
        clientes = self.cursor.fetchall()
        return [Clientes(*cliente) for cliente in clientes]
    
    def buscar_cliente_por_email(self, email):
        self.cursor.execute('''SELECT * FROM Clientes WHERE email = ?''', (email,))
        cliente = self.cursor.fetchone()
        if cliente:
            return Clientes(*cliente)
        else:
            return None
        
    def atualizar_status_cliente(self, email):
        cliente = self.buscar_cliente_por_email(email)
        if cliente:
            self.cursor.execute('''UPDATE Clientes SET status = ? WHERE email = ?''', (0, email))
            self.conexao.commit()
            print(f"Status do cliente com o e-mail: {email} atualizado com sucesso para inativo.", end="\n\n")
        else:
            print("E-mail de cliente não encontrado.", end="\n\n")

    def buscar_clientes_inativos(self):
        self.cursor.execute('''SELECT * FROM Clientes WHERE status = ?''', (0,))
        cliente = self.cursor.fetchone()
        if cliente:
            return Clientes(*cliente)
        else:
            return None
        
    def excluir_clientes_inativos(self):
        cliente = self.buscar_clientes_inativos()
        if cliente:
            self.cursor.execute('''DELETE FROM Clientes WHERE status = ?''', (0,))
            self.conexao.commit()
            print("Clientes inativos excluídos com sucesso.", end="\n\n")
        else:
            print("Clientes inativos não encontrados.", end="\n\n")

banco = BancoDeDados("banco_clientes.sqlite")
banco.conectar()
banco.criar_tabela()
# Inserindo alguns clientes incluindo o cliente pedido na prova:
banco.inserir_cliente("Ana Silva", "ana.silva@gmail.com", "2023-02-16", True)
banco.inserir_cliente("João Silva", "joao.silva@gmail.com", "2023-02-16", False)
banco.inserir_cliente("Maria Silva", "maria.silva@gmail.com", "2023-02-16", False)
banco.inserir_cliente("José Silva", "jose.silva@gmail.com", "2023-02-16", True)
# Mostrando os dados da tabela:
clientes = banco.selecionar_clientes()
print("Dados atuais da tabela:", end="\n\n")
for cliente in clientes:
    print (f"Nome.............: {cliente.nome}")
    print (f"E-mail...........: {cliente.email}")
    print (f"Data de cadastro.: {cliente.data_cadastro}")
    print (f"Status...........: {'Ativo' if cliente.status else 'Inativo'}")
    print("+" * 30)
pausar()
limpar_tela()
# Selecionando o nome e o email de todos os clientes ativos.
clientes_ativos = banco.selecionar_clientes_ativos()
print("Selecionando clientes ativos", end="\n\n")
for cliente in clientes_ativos:
    print (f"Nome.............: {cliente.nome}")
    print (f"E-mail...........: {cliente.email}")
    print("+" * 30)
print("Nome e e-mail de clientes ativos listados", end="\n\n")
pausar()
limpar_tela()
# Atualizando o status do cliente com o email "ana.silva@gmail.com" para inativo.
# Depois mostrando novamente os dados da tabela
banco.atualizar_status_cliente("ana.silva@gmail.com")
clientes = banco.selecionar_clientes()
print("Dados atuais da tabela:", end="\n\n")
for cliente in clientes:
    print (f"Nome.............: {cliente.nome}")
    print (f"E-mail...........: {cliente.email}")
    print (f"Data de cadastro.: {cliente.data_cadastro}")
    print (f"Status...........: {'Ativo' if cliente.status else 'Inativo'}")
    print("+" * 30)
pausar()
limpar_tela()
# Deletando todos os clientes inativos da tabela.
# Depois mostrando novamente os dados da tabela no final.
banco.excluir_clientes_inativos()
clientes = banco.selecionar_clientes()
print()
print("Dados atuais da tabela:", end="\n\n")
for cliente in clientes:
    print (f"Nome.............: {cliente.nome}")
    print (f"E-mail...........: {cliente.email}")
    print (f"Data de cadastro.: {cliente.data_cadastro}")
    print (f"Status...........: {'Ativo' if cliente.status else 'Inativo'}")
    print("+" * 30)
print()