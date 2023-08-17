'''import math
num = float(input('Digite um número: '))
print('sua porção inteira é {}'.format(math.trunc(num)))

num = float(input('Digite um valor: '))
n = int(num)
print('A parte inteira do valor {} corresponde a {}'.format(num, n))'''

from math import trunc
num = float(input('Digite um valor: '))
print('A porção inteira do valor {} é {}'.format(num, trunc(num)))

#módulo math = módulo matemático 
#import trunc > retorna as partes inteiras truncadas de um número e não arredonda o número, mas remove os decimais

#tem que importar a biblioteca math para poder usar o módulo trunc 
print(math.trunc(2.77))
