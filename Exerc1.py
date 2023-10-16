def media_de_notas(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 6:
        print('Você foi Aprovado')
    else:
        print('Você foi Reprovado')

n1 = int(input('Insira o valor da Primeira nota: '))
n2 = int(input('Insira o valor da Segunda nota: '))

media_de_notas(n1, n2)
