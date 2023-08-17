# >Programa que leia a altura e a largura de uma parede em metros
# >Calcule sua área e a quantidade de tinta necessária 
# >Cada litro de tinta pinta uma área de 2m quadrados

largura = float(input(' Quantos metros de largura:'))
altura = float(input('Quantos metros de altura: '))
A = altura * largura
print('A área da parede equivale a {:.2f}m²'.format(A))
tinta = A / 2
print('Cada litro de tinta vocÊ precisará de {:.2f}L.'.format(tinta))