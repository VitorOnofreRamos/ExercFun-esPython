"""
Tabuada de um número
"""

def ler_numero():
    numero = int(input('Digite um Número Inteiro: '))
    return numero

def tabuada(n):
    for i in range(1, 11):
        valor = n * i
        print(valor)

tabuada(ler_numero())
