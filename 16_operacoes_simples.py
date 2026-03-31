'''Desenvolva um sistema que solicite dois números ao usuário.
Objetivo: O sistema deve perguntar ao usuário qual das cinco operações aritméticas (soma, subtração, divisão, multiplicação e exponenciação) deseja realizar com os dois números e exibir os resultados.
Regra: Use funções para realizar as operações
'''
n1=int(input("digite o primeiro numero"))
n2=int(input("digite o segundo numero"))
op= input('escolha a operação')
if op=='+':
    print(n1+n2)
elif op=='-':
    print(n1-n2)
elif op=='/':
    print(n1/n2)
elif op=='*':
    print(n1*n2)
elif op=='**':
    print(n1**n2)