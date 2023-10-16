"""
Números de lados de um polígono
"""

def descobrir_poligono(numerodelados):
    match numerodelados:
        case 3:
            print('TRIÂNGULO')
        case 4:
            print('QUADRILÁTERO')
        case 5:
            print('PENTÁGONO')
        case _:
            print('VALOR INVÁLIDO')

n = int(input('Digite um número: '))

descobrir_poligono(n)
