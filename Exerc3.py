"""
Dobro de um Número
"""

def numero_dobro(numero):
    numero *= 2
    return numero

n = int(input('Digite um número: '))

print(f'O dobro de {n} é {numero_dobro(n)}')
