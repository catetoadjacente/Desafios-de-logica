'''Ewerton e Rodrigo estão discutindo sobre quem foi o aluno favorito do professor João. Como não conseguem chegar a um acordo, decidem resolver a disputa no “par ou ímpar”.
Objetivo: Desenvolver um programa que receba um número e informe se ele é par ou ímpar.
Regra: Um número é par quando é divisível por 2. Caso contrário, ele é ímpar. O sistema deve continuar a realizar verificações de par ou ímpar até que o usuário interrompa sua execução.
'''
n1 = int(input('digite o número'))
while True:
	if n1 % 2 == 0:
		print('O número é par')
	else:
		print('O número é ímpar')
	n1 = int(input('digite o número'))