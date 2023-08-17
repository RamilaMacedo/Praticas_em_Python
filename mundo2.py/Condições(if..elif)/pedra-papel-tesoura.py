"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import randint
from time import sleep
itens = ('Pedra', 'papel', 'Tesoura')
computador = randint(0, 2)
print('''Sua Opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('>'*20)
print('Computador jogou', itens[computador])
print('Jogador jogou', itens[jogador])
print('<'*20)
if computador == 0: #computador jogou pedra de acordo com as opções la em cima
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('OPÇÃO INVÁLIDA')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('OPÇÃO INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('OPÇÃO INVÁLIDA')