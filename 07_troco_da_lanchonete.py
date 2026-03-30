'''Daniel foi na padaria biju comprar um lanche. 
Desenvolva um sistema que receba o valor do lanche e o valor que Daniel pagou e por fim calcule o troco que Daniel deverá receber da padaria.
'''
valor_lanche = int(input("valor do lanche: "))
valor_pago = int(input("valor pago: "))

if valor_pago >= valor_lanche:
    troco = valor_pago - valor_lanche
    print("O troco de é:", troco,'R$')
else:
    falta = valor_lanche - valor_pago
    print('Faltam', falta,'R$')