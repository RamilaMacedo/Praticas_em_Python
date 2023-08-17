"""
 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
 > se ele ainda vai se alistar ao serviço militar
 > se é a hora exata de se alistar
 > se já passou do tempo do alistamento. 
 
 *Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date
print('\33[4;33mData de Nascimento\33[m')
dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade == 18:
    print('Você está pronto para o alistamneto do serviço militar')
elif idade > 18:
    restante = idade - 18
    print('VocÊ deveria ter se alistado ha {} anos. Infelizmento seu prazo inspirou'.format(restante))
    ano = atual - restante
    print('Seu alistamento foi em {}'.format(ano))
elif idade < 18:
    restante = 18 - idade
    print('Calma, não é o momento para se alistar no serviço militar, ainda faltam {} anos'.format(restante))
    ano = restante - atual
    print('Seu alistamento será no ano de {}'.format(ano))