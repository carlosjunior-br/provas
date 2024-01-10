"""
[PY-A13] Classe Bomba de Combustível:
Faça um programa completo utilizando classes e métodos que:
Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
i.tipoCombustivel.
ii.valorLitro
iii.quantidadeCombustivel
Possua no mínimo esses métodos:
i.abastecerPorValor( )
método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
ii.abastecerPorLitro( )
     –    método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
iii. alterarValor( )
     –    altera o valor do litro do combustível.
iv. alterarCombustivel( )
     –     altera o tipo do combustível.
v.  alterarQuantidadeCombustivel( )
     –     altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba
"""
class BombaCombustivel:
    def __init__(self, TipoCombustivel: str, ValorLitro: float, QuantidadeCombustivel: float):
        self.TipoCombustivel = TipoCombustivel
        self.ValorLitro = ValorLitro
        self.QuantidadeCombustivel = QuantidadeCombustivel

    def AbastecerPorValor(self, valor: float):
        litros = round(valor / self.ValorLitro, 2)
        print(f"Foi solicitado {litros:.2f} litros de {self.TipoCombustivel}...")
        if self.QuantidadeCombustivel >= litros:
            self.QuantidadeCombustivel -= litros
            print(f"Abastecimento realizado com sucesso! Foi colocado {litros:.2f} litros no veículo.")
        else:
            print(f"Abastecimento não realizado! Bomba com quantidade insuficiente.")

    def AbastecerPorLitro(self, litros: float):
        valor = round(self.ValorLitro * litros, 2)
        print(f"Foi solicitado {litros:.2f} litros de {self.TipoCombustivel}...")
        if self.QuantidadeCombustivel >= litros:
            self.QuantidadeCombustivel -= litros
            print(f"Abastecimento realizado com sucesso! Valor a ser pago: R$ {valor:.2f}.")
        else:
            print(f"Abastecimento não realizado! Bomba com quantidade insuficiente.")

    def AlterarValor(self, valor):
        ValorAnterior = self.ValorLitro
        self.ValorLitro = valor
        print("=" * 50)
        print(f"O valor por litro foi alterado com sucesso!")
        print(f"Valor anterior: R$ {ValorAnterior:.2f}.")
        print(f"Valor atual...: R$ {self.ValorLitro:.2f}.")
        print("=" * 50)

    def AlterarCombustivel(self, tipo: str):
        TipoAnterior = self.TipoCombustivel
        self.TipoCombustivel = tipo
        print("=" * 50)
        print(f"O tipo de combustível foi alterado com sucesso!")
        print(f"Combustível anterior: {TipoAnterior}.")
        print(f"Combustível atual...: {self.TipoCombustivel}.")
        print("=" * 50)

    def AlterarQuantidadeCombustivel(self, quant: float):
        QuantAnterior = self.QuantidadeCombustivel
        self.QuantidadeCombustivel = quant
        print("=" * 50)
        print(f"A quantidade de combustível restante na bomba foi alterada com sucesso!")
        print(f"Quantidade anterior: {QuantAnterior:.2f} litros.")
        print(f"Quantidade atual...: {self.QuantidadeCombustivel:.2f} litros.")
        print("=" * 50)
    
    def ExibirDadosBomba(self):
        print("=" * 50)
        print(f"Tipo de combustível......: {self.TipoCombustivel}.")
        print(f"Valor do litro...........: R$ {self.ValorLitro:.2f}.")
        print(f"Quantidade de combustível: {self.QuantidadeCombustivel:.2f} litros.")
        print("=" * 50)

# Uso da classe e métodos:
        
bomba1 = BombaCombustivel("Gasolina", 4.80, 200)
bomba1.ExibirDadosBomba()
bomba1.AbastecerPorValor(100)
bomba1.ExibirDadosBomba()
bomba1.AbastecerPorLitro(30)
bomba1.ExibirDadosBomba()
bomba1.AlterarCombustivel("Etanol")
bomba1.AlterarValor(3.80)
bomba1.AbastecerPorValor(100)
bomba1.ExibirDadosBomba()
bomba1.AlterarQuantidadeCombustivel(200)
bomba1.AbastecerPorLitro(35)
bomba1.ExibirDadosBomba()