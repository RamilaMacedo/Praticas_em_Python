"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIO
– Acima de 25 anos: MASTER
"""

from datetime import date
from time import sleep
print('\33[33mSelecionando categoria para Seleção de Natação\33[m')
print('\33[34m-\33[m'*15)
ano = int(input('Ano de Nascimento: '))
idade = date.today().year - ano
print(f'Você tem {idade} anos')
print('...\33[2;31mUM MOMENTO, VERIFICANDO!!\33[m')
sleep(3)
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:=
    print('Sua categoria é JÚNIOR')
elif idade <= 25:
    print('Sua categoria é SÊNIOR')
elif idade >= 25:
    print('Sua categoria é MASTER')