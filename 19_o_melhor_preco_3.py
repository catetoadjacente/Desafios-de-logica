'''D. Joana está no supermercado e ficou em dúvida sobre qual amaciante de roupas seria o mais barato
Objetivo: Desenvolva um sistema que receba os dois nomes e valores e volume, dos amaciantes, informados pelo usuário e indique qual deles é o mais barato.
Regras: O sistema deve exibir claramente qual dos dois valores é o maior. Caso os valores sejam iguais, o sistema deve informar que ambos possuem o mesmo valor. Os valores podem ser inteiros ou decimais.
'''
am1 = input('nome amaciante 1 ')
am2 = input('nome amaciante 2 ')
valor_am1 = int(input('valor amaciante 1 '))
valor_am2 = int(input('valor amaciante 2 '))
volume_am1 = int(input('volume amaciante 1 '))
volume_am2 = int(input('volume amaciante 2 '))
preco_por_litro_am1 = valor_am1 / volume_am1
preco_por_litro_am2 = valor_am2 / volume_am2
if preco_por_litro_am1 < preco_por_litro_am2:
    print('o amaciante', am1, 'é mais barato')
elif preco_por_litro_am2 < preco_por_litro_am1:
    print('o amaciante', am2, 'é mais barato')
else:
    print('ambos os amaciantes possuem o mesmo valor')

