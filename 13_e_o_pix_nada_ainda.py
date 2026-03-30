'''Um certo competidor com nome iniciando com P. Recebe R$ 60,20 por hora trabalhada. 
Se ele trabalhar mais que 20 horas receberá um adicional de 30%, de hora extra.
Objetivo: Desenvolva um sistema que calcule quanto este determinado competidor recebe ao fim do mês caso faça ou não horas extras no mês.
Regras: O adicional se aplica apenas sobre as horas que superem as 20h regulares de trabalho.
'''
horas_trabalhadas = int(input('Digite quantas horas foram trabalhadas '))
ganho = horas_trabalhadas * 60.20
if horas_trabalhadas > 20:
    hora_extra = horas_trabalhadas- 20
    print('o competidor p, recebeu', (hora_extra*(30/100)))
else:
    print('o competidor p recebeu', ganho)     