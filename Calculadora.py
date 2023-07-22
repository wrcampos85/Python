from interface import *
from time import sleep

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
maior = 0
while True:
    resposta = menu(['ADIÇÃO', 'SUBTRAÇÃO', 'MULTIPLICAÇÃO', 'DIVISÃO', 'PORCENTAGEM', 'MAIOR', 'NOVOS NÚMEROS', 'SAIR DO SISTEMA'])
    if resposta == 1:
        sleep(2)
        print(f'A adição de {n1} + {n2} é igual há: {n1 + n2:.0f}')
    elif resposta == 2:
        sleep(2)
        print(f'A subtração de {n1} - {n2} é igual há: {n1 - n2:.0f}')
    elif resposta == 3:
        sleep(2)
        print(f'A multiplicação de {n1} x {n2} é igual há: {n1 * n2:.0f}')
    elif resposta == 4:
        sleep(2)
        print(f'A divisão de {n1} por {n2} é igual há: {n1/n2:.0f}')
    elif resposta == 5:
        sleep(2)
        print(f'{n1} por cento de {n2} é igual há: {n1 * n2 /100:.0f}')
    elif resposta == 6:
        if n1 > maior and n1 > n2:
            maior = n1
        else:
            maior = n2
            sleep(1)
        print(f'Entre {n1} e {n2} o mai número é: {maior} ')
    elif resposta == 7:
        sleep(1)
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif resposta == 8:
        print('Saindo do programa...')
        break
