'''Na escola, a matéria favorita de Marcelo sempre foi matemática. Ele sempre ficou intrigado com a existência dos triângulos e com as regras que determinam se três segmentos de reta podem ou não formar um triângulo.
Objetivo: Desenvolver um programa que receba o comprimento de três retas e verifique se elas podem formar um triângulo. Caso possam, o programa deve informar qual é o tipo de triângulo formado: equilátero, isósceles ou escaleno.
Regras: Para que três retas formem um triângulo, a soma dos comprimentos de dois lados deve ser maior que o comprimento do terceiro lado, para todas as combinações possíveis. Se for possível formar um triângulo: O triângulo será equilátero se os três lados forem iguais. O triângulo será isósceles se dois lados forem iguais e um diferente. O triângulo será escaleno se todos os lados forem diferentes.
'''
medida_segmento_de_reta_1 = int(input('Medida do segmento de reta 1'))
medida_segmento_de_reta_2 = int(input('Medida do segmento de reta 2'))
medida_segmento_de_reta_3 = int(input('Medida do segmento de reta 3'))
if medida_segmento_de_reta_1 == medida_segmento_de_reta_2 == medida_segmento_de_reta_3:
    print('Triângulo equilátero')
elif medida_segmento_de_reta_1 == medida_segmento_de_reta_2 or medida_segmento_de_reta_1 == medida_segmento_de_reta_3 or medida_segmento_de_reta_2 == medida_segmento_de_reta_3:
    print('triângulo isóceles')

