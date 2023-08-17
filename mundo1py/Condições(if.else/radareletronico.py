"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

from time import sleep
print('='*20)
print('Em uma Br onde a velocidade permitida é 80km/h...')
print('='*20)
V = int(input('Qual a Velocidade do seu carro: '))
if V > 80:
    print('Você ultrapassou o limite máximo de 80 km/h, vc foi MULTADO!')
    print('CALCULANDO SUA MULTA...')
    sleep(3)
    multa = (V - 80) * 7
    print('Sua multa vai custar R${}'.format(multa))
else:
    print('Limite permitido, tenha um bom dia!')
