"""
Calculadora
"""

def menu():

    opcao = int(input('Calculadora\r\n'
          '1 - Adição\r\n'
          '2 - Subtração\r\n'
          '3 - Multiplicação\r\n'
          '4 - Divisão\r\n'
          '5 - Sair do programa\r\n'
          'Selecione sua opção: '))

    match opcao:
        case 1:
            print(f'O resultado é igual a {adicao()}')
        case 2:
            print(f'O resultado é igual a {subtracao()}')
        case 3:
            print(f'O resultado é igual a {multiplicacao()}')
        case 4:
            print(f'O resultado é igual a {divisao()}')
        case 5:
            print("Finalizando programa...")
            return False
        case _:
            print("Opção inválida")

def adicao():
    numero1 = int(input('Digite o primeiro número que deseja Somar: '))
    numero2 = int(input('Digite o segundo número que deseja Somar: '))
    valor = numero1 + numero2
    return valor

def subtracao():
    numero1 = int(input('Digite o primeiro número que deseja Subtrair: '))
    numero2 = int(input('Digite o segundo número que deseja Subtrair: '))
    valor = numero1 - numero2
    return valor

def multiplicacao():
    numero1 = int(input('Digite o primeiro número que deseja Multiplicar: '))
    numero2 = int(input('Digite o segundo número que deseja Multiplicar: '))
    valor = numero1 * numero2
    return valor

def divisao():
    numero1 = int(input('Digite o primeiro número que deseja Dividir: '))
    numero2 = int(input('Digite o segundo número que deseja Dividir: '))
    
    while numero2 == 0:
        numero2 = int(input('Impossível realizar uma Divisão por zero, por favor digite outro número: '))

    valor = numero1 / numero2
    return valor

while True:
    if menu() == False:
        break
