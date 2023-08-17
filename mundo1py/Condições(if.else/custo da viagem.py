"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
"""

d = float(input('Me diga qual a distancia vc irá percorrer: '))
p1 = d * 0.50
p2 = d * 0.45
if d <= 200:
    print('Sua passagem custará R${:.2f}'.format(p1))
else:
    print('Sua passarem custara R${:.2f}'.format(p2))
#tambem pode ser feito da seguinte maneira
'''preço = distância * 0.50 if  distancia <= 200 else distância * 0.45'''