"""
Peso Ideal
"""

def peso_ideal(altura, sexo):
    if sexo.upper() == 'F':
        valor = 62.1 * altura - 44.7
    elif sexo.upper() == 'M':
        valor = 72.7 * altura - 58
    else:
        print('A informação referente ao sexo está de formato incorreto')
        peso = None
    return valor

n = float(input('Digite sua altura em metros: '))
s = input('Digite o seu Sexo (M)/(F): ')

print(f'O seu Peso Ideal é {peso_ideal(n, s):.2f}')
