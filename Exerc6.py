def peso_ideal(altura, sexo):
    if sexo == 'F':
        valor = 62.1 * altura - 44.7
    else:
        valor = 72.7 * altura - 58
    return valor

n = float(input('Digite sua altura em metros: '))
s = input('Digite o seu Sexo: ')

print(f'{peso_ideal(n, s):.2f}')
