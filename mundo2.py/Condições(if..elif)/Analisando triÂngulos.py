"""
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
"""

#Analisando os triângulos

l1 = float(input('primeiro segmento:'))
l2 = float(input('segundo segmento:'))
l3 = float(input('terceiro segmento:'))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos formam um triângulo', end= '')
    if l1 != l2 != l3 != l1:
        print('escaleno') #todos os lados são diferentes
    elif l1 == l2 == l3:
        print('Equilátero') #todos os lados são iguais
    else:
        print('Isóceles') #dois lados são iguais e um diferente
else:
    print('Não podem formar um triângulo')
