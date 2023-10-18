"""
Área e Perimetro de um Círculo
"""

import math

def area(raio):
    valor = math.pi * raio ** 2
    return valor

def perimetro(raio):
    valor = math.pi * 2 * raio
    return valor

n = int(input('Digite um número: '))

print(f'A área de um Círculo com raio de {5} é {area(n):.2f};\r\n'
      f'O perimetro de um Círuclo com raio de {5} é {perimetro(n):.2f}.')
