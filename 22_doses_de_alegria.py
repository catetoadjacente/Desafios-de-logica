'''Sendo hoje véspera da véspera de sexta-feira, José resolveu sair para comemorar após o curso. Depois de algumas doses de alegria líquida, chegou a hora de pagar a conta.
Objetivo: Desenvolver um programa que receba o valor disponível na conta de José e o valor gasto com as doses de alegria líquida, e informe se o saldo da conta:
#Continuou positivo
#Ficou zerado (e quanta falta para chegar ao valor gasto) 
#Ou foi para o negativo
'''
valor_bebida = int(input('valor da bebida '))
valor_em_conta = int(input('digite o valor disponivel '))
if valor_em_conta - valor_bebida > 0:
    print('saldo positivo')
elif valor_em_conta - valor_bebida == 0:
    print(f'saldo zerado, faltam {valor_bebida - valor_em_conta} R$')
else:
    print(f'saldo negativo, falta {valor_bebida - valor_em_conta} R$')

