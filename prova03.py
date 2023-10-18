"""
[PY-A02] - Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista. Em seguida, o programa
deve separar os números pares e ímpares em listas diferentes. Por fim, exiba na tela os números pares, os números ímpares
em uma tupla, a quantidade de números pares e ímpares presentes na lista, e a soma de todos os números pares e ímpares,
respectivamente.
"""
lista_de_numeros = []
numeros_pares = []
numeros_impares = []

# Solicite ao usuário que digite 10 valores para preencher uma lista
for n in range(10):
    recebe_valores = int(input(f"Digite o {n+1}º valor: "))
    lista_de_numeros.append(recebe_valores)

# Separar os números pares e ímpares em listas diferentes
for n in lista_de_numeros:
    if n % 2 == 0:
        numeros_pares.append(n)
    else:
        numeros_impares.append(n)

# Exiba na tela os números pares, os números ímpares em uma tupla
tupla_numeros_pares = tuple(numeros_pares)
tupla_numeros_impares = tuple(numeros_impares)
print(" ")
print("Números pares: ", tupla_numeros_pares, end="\n\n")
print("Números ímpares: ", tupla_numeros_impares, end="\n\n")

# Quantidade de números pares e ímpares presentes na lista
print("Quantidade de números pares presentes na lista: ", len(numeros_pares), end="\n\n")
print("Quantidade de números ímpares presentes na lista: ", len(numeros_impares), end="\n\n")

# Soma de todos os números pares e ímpares, respectivamente
print("A soma de todos os números pares presentes na lista é: ", sum(numeros_pares), end="\n\n")
print("A soma de todos os números ímpares presentes na lista é: ", sum(numeros_impares))