"""
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""


from time import sleep
print('-0-' * 20)
print('Adivinhe um número que estou pensando:...')
print('-0-'* 20)
n = int(input('Tente adivinhar um número de 0...5 e veja se acertou: '))
print('PROCESSANDO...')
sleep(3)
print('VOCÊ VENCEU' if n == 2 else'VOCÊ PERDEU')
if n == 2:
    print('PARABENS, VOCê VENCEU')
else:
    print('UMA PENA, EU ESCOLHI O NÚMERO 2, O COMPUTADOR VENCEU')

from random import randint #randint é um método que retorna um elemento selecionado entre o intervalo especifico
#geração de número pseudo-aleatórios
computador = randint(0, 5) # esse módulo faz o computador# 'pensar'
print('=n=' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('=n=' * 20)
jogador = int(input('Em que número eu pensei? '))
if computador == jogador:
    print('PARABENS, VOCÊ ME VENCEU')
else:
    print('Pena, eu escolhi o número {} e não {}'.format(computador, jogador))