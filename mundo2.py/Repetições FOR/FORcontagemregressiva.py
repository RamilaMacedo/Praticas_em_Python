"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""


#contagem regressiva de 0 a 10 usando tempo de espera e repetição
from time import sleep
print('{:^40}'.format('CONTAGEM REGRESSIVA'))
for fogos in range(10, -1, -1):

    print(fogos)
    sleep(1)
print('FOGOOOOSSSS ')

