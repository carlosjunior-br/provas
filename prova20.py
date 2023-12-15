"""
[PY-A11] Você foi contratado para desenvolver o software de controle de um elevador inteligente. A classe Elevador foi
criada para modelar esse sistema e possui os seguintes atributos: totalCapacidade, atualCapacidade, totalAndar e atualAndar,
que representam, respectivamente, a capacidade máxima do elevador, a capacidade atual, o total de andares do prédio e o andar
atual do elevador.
A classe Elevador também possui os seguintes métodos:
Subir(): caso o elevador não esteja no andar mais alto, o método incrementa o número do andar atual e exibe "Subindo".
Caso contrário, exibe "VOCÊ ESTÁ NO ANDAR MAIS ALTO!".
Descer(): caso o elevador não esteja no térreo, o método decrementa o número do andar atual e exibe "Descendo". Caso contrário,
exibe "VOCÊ JÁ ESTÁ NO TÉRREO!".
Entrar(): caso a capacidade atual do elevador não tenha sido atingida, o método incrementa o número de pessoas presentes no
elevador e exibe "Entrando uma pessoa". Caso contrário, exibe "O ELEVADOR ESTÁ CHEIO!".
Sair(): caso haja pelo menos uma pessoa no elevador, o método decrementa o número de pessoas presentes e exibe "Saindo uma
pessoa". Caso contrário, exibe "NÃO TEM NINGUÉM".
"""
class Elevador():
    def __init__(self, totalCapacidade, totalAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = 0
        self.totalAndar = totalAndar
        self.atualAndar = 0

    def Subir(self):
        if self.atualAndar != self.totalAndar:
                self.atualAndar += 1
                print(f"SUBINDO. O ANDAR ATUAL AGORA É {self.atualAndar}.")
        else:
            print(f"VOCÊ ESTÁ NO ANDAR MAIS ALTO!")

    def Descer(self):
        if self.atualAndar != 0:
            self.atualAndar -=1
            print(f"DESCENDO. O ANDAR ATUAL AGORA É {self.atualAndar}.")
        else:
            print(f"VOCÊ JÁ ESTÁ NO TÉRREO!")

    def Entrar(self):
        if self.totalCapacidade > self.atualCapacidade:
            self.atualCapacidade += 1
            print(f"ENTRANDO UMA PESSOA. AGORA TEM {self.atualCapacidade} PESSOA(S) NO ELEVADOR.")
        else:
            print(f"O ELEVADOR ESTÁ CHEIO!")

    def Sair(self):
        if self.atualCapacidade > 0:
            self.atualCapacidade -= 1
            print(f"SAINDO UMA PESSOA. AGORA TEM {self.atualCapacidade} PESSOA(S) NO ELEVADOR.")
        else:
            print(f"NÃO TEM NINGUÉM!")

# Exemplo do uso:
elevador1 = Elevador(10, 5)
elevador1.Entrar()
elevador1.Subir()
elevador1.Sair()
elevador1.Entrar()
elevador1.Entrar()
elevador1.Entrar()
elevador1.Subir()
elevador1.Subir()
elevador1.Sair()
elevador1.Descer()
elevador1.Descer()
elevador1.Descer()
elevador1.Sair()
elevador1.Sair()
elevador1.Sair()