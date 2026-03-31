'''D. Joana está no supermercado e ficou em dúvida sobre qual amaciante de roupas seria o mais barato
Objetivo: Desenvolva um sistema que receba os dois nomes e valores, dos amaciantes, informados pelo usuário e indique qual deles é o mais barato.
Regras: O sistema deve exibir claramente qual dos dois valores é o maior. Caso os valores sejam iguais, o sistema deve informar que ambos possuem o mesmo valor. Os valores podem ser inteiros ou decimais.
'''
am1 = input('nome amaciante 1')
am2 = input('nome amaciante 2')
valam1 = int(input('valor amaciante 1'))
valam2 = int(input('valor amaciante 2'))
if valam1 < valam2:
    print('o amaciante', am1, 'é mais barato')
elif valam2 < valam1:
    print('o amaciante', am2, 'é mais barato')
else:
    print('ambos os amaciantes possuem o mesmo valor')
