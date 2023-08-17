# >Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# >Calcule e mostre o comprimento da hipotenusa

'''co = int(input('Digite um valor para o cateto oposto:'))
ca = int(input(' Digite um valor para o cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('Calculando a hipotenusa, a²+b²=c², seu comprimento vale {:.3f}'.format(hi))'''

from math import hypot
co = int(input(" Digite um valor para o cateto oposto:"))
ca = int(input(' Digite um valor para o cateto adjacente:'))
print('Calculando a hipotenusa seu valor é {:.2f}'.format(hypot(co, ca)))

#math.hipot> retorna norma euclidiana
#Norma Euclidiana: é a distância da origem às coordenadas dadas. É derivada do teorema de pitágoras
#O teorema afirma que um triângulo retangulo, o quadrado  do comprimento da hipotenusa é igual à soma dos quadrados dos outros dois lados.
