'''O supermercado Líder está embalando maçãs em caixas para transporte entre filiais. Cada caixa comporta até 12 maçãs.z
Objetivo: Desenvolver um programa que receba a quantidade total de maçãs a serem embaladas e informe quantas caixas serão necessárias para concluir o empacotamento. 
Regras:Cada caixa pode conter, no máximo, 12 maçãs.Todas as maçãs devem ser embaladas, mesmo que a última caixa não fique completamente cheia.
'''
n_maçãs = int(input('quantas maças existem? '))
caixas = n_maçãs//12
resto = n_maçãs%12
if resto > 0:
    caixas = caixas + 1
    print(f'serão necessarias {caixas} caixas')