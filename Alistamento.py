ano = int(input('Ano de nascimento: '))
idade = 2017 - ano
alistamento = idade - 18
anoa = 2017 - alistamento
maioridade = 18 - idade
print(f'Quem nasceu em {ano} tem {idade} anos em 2017.')
if idade > 18:
    print(f'Você já deveria ter se alistado há {alistamento} anos.')
    print(f'Seu alistamento foi em {anoa}.')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
else:
    print(f'Ainda faltam {maioridade} anos para o alistamento.')
    print(f'Seu alistamento será em {anoa}.')
