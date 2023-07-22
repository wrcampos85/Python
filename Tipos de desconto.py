from interface import *

cabeçalho('LOJAS TABAJARA')
preço = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
desc10 = (preço * 10) / 100
desc5 = (preço * 5) / 100
juros = (preço * 20) / 100
while True:
    print('Qual é a forma de pagamento? ')
    resposta = menu(['dinheiro/ cheque à vista', 'à vista no cartão', '2x no cartão', '3x ou mais no cartão'])
    if resposta == 1:
        print(f'Sua compra de R${preço:.2f} vai custar R${preço - desc10:.2f} à vista.')
        break
    elif resposta == 2:
        print(f'Sua compra de R${preço:.2f} vai custar R${preço - desc5:.2f} à vista no cartão.')
        break
    elif resposta == 3:
        print(f'Sua compra de R${preço:.2f} vai ser parcelada em 2x de R${preço / 2:.2f}')
        break
    elif resposta == 4:
        parcelas = int(input('Quantas parcelas? '))
        if parcelas <= 2:
            print('ERRO, favor informar parcelas acima de 3 vezes ')
        else:
            print(f'Sua compra será parcelada em {parcelas}x de R${(preço + juros) / parcelas:.2f} com juros')
            print(f'Sua compra de R${preço:.2f} vai custar R${preço + juros:.2f} no final.')
            break