'''Na marinha, Emanuel era responsável por acompanhar o desempenho dos militares durante os treinamentos de natação. 
Para isso, ele precisava registrar o tempo de cada marinheiro e avaliar se o resultado foi satisfatório.
Objetivo: Desenvolver um programa que receba a graduação de um militar e o tempo (em segundos) que ele levou para concluir uma prova de natação. 
O sistema deve verificar se a graduação é válida e, em seguida, avaliar o desempenho do militar com base no tempo informado.
Regras: Validação de graduação: O sistema deve aceitar apenas as graduações válidas da Marinha do Brasil. 
Avaliação do tempo de prova: Se o tempo for maior que 40 segundos, o desempenho é considerado muito ruim. 
Se o tempo estiver entre 30 e 40 segundos (inclusive), o desempenho está bom, mas pode melhorar. Se o tempo for menor que 30 segundos, o desempenho é excelente.
'''
graduação = input('Digite a graduação do militar ')
tempo = int(input('tempo que o militar levou para concluir a prova '))
graduaçoes_validas = ["marinheiro", "cabo", "terceiro-sargento", "segundo-sargento", "primeiro-sargento", "suboficial", "segundo-tenente", "primeiro-tenente", "capitão-tenente"]
if graduação not in graduaçoes_validas:
    print("graduação não válida" )
if tempo > 40:
    print('Desempenho muito ruim.')
elif 30 <= tempo <= 40:
    print('Desempenho bom, mas pode melhorar.')
else:
    print('Desempenho excelente.')