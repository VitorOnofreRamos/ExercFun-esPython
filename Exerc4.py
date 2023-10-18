"""
Par ou Impar
"""

def par_ou_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

n = int(input('Digite um número: '))

if par_ou_impar == True:
    print(f"O númeor '{n}' é Par")
elif par_ou_impar == False:
    print(f"O númeor '{n}' é Impar")