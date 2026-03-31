'''D. Joana está no supermercado e ficou em dúvida sobre qual amaciante de roupas seria o mais barato
Objetivo: Desenvolva um sistema que receba os dois valores, dos amaciantes, informados pelo usuário e indique qual deles é o mais barato.
Regras: O sistema deve exibir claramente qual dos dois valores é o mais barato. Caso os valores sejam iguais, o sistema deve informar que ambos possuem o mesmo valor. Os valores podem ser inteiros ou decimais.
'''
am1 = int(input('valor amaciante 1'))
am2 = int(input('valor amaciante 2'))
if am1 < am2:
    print('o amaciante 1 é mais barato')
else:
    print('o amaciante 2 é mais barato')