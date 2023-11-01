"""
[PY-A05] Considere uma lista de números inteiros 

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Utilizando as funções map(),filter() e reduce(), escreva um código que execute as seguintes operações:

Função map() para obter uma nova lista com o quadrado de cada número da lista numeros

Função filter() para obter uma nova lista com números pares da lista numeros

Função reduce()  para obter a soma de todos os números da lista numeros

Qual o resultado obtido após a execução das operações acima?
"""
from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista de números: ", numeros)
print("----------------------------------------------------------------")

# Função map() para obter uma nova lista com o quadrado de cada número da lista numeros
Resultado1 = list(map(lambda x: x ** 2, numeros))
print("Nova lista com o quadrado de cada número da lista numeros:")
print(Resultado1)
print("----------------------------------------------------------------")

# Função filter() para obter uma nova lista com números pares da lista numeros
Resultado2 = list(filter(lambda x: x % 2 == 0, numeros))
print("Nova lista com números pares da lista numeros:")
print(Resultado2)
print("----------------------------------------------------------------")

# Função filter() para obter uma nova lista com números pares da lista numeros
Resultado3 = reduce(lambda x, y: x + y, numeros)
print("Obter a soma de todos os números da lista numeros:")
print(Resultado3)
print("----------------------------------------------------------------")