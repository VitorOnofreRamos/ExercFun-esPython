def par_ou_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

n = int(input('Digite um número: '))

print(f'{par_ou_impar(n)}')
