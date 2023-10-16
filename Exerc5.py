import math

def area(raio):
    valor = math.pi * raio ** 2
    return valor

def perimetro(raio):
    valor = math.pi * 2 * raio
    return valor

n = int(input('Digite um número: '))

print(f'{area(n):.2f}, {perimetro(n):.2f}')
