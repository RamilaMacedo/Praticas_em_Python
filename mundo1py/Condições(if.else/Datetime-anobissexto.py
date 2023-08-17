"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""


from datetime import date
ano = int(input('Digite um ano:'))
if ano == 0:
    ano = date.today().year
print('Me diga se ele é um ano bissexto...')
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))


"""
RETORNA O ANO E O DIA DA SEMANA
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A")) #%A especifica algo sobre o tempo /hora/ dia/data/minutos/ todas tem uma sigla que da referencia
EXEMPLO:

%a > dia da semana abreviado
%A > dia da semana por extenso
%b/%B > mês abreviado/extenso
%Y > ano
"""



