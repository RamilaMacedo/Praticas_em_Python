"""
Um algoritmo que leia um número e mostre seu dobro/triplo/raiz quadrada
"""

n = int(input('Digite um número: '))
print('o dobro de {} é? {}'.format(n,n*2))
print('o triplo de {} é ? {}'.format(n,n*3))
print('a raiz quadra de {} é? {:.2}'.format(n,n**(1/2)))

n = int(input('Digite um número inteiro: '))
d = n * 2
t = n * 3
rq = n ** (1/2)
print('o dobro de {} é {}, o triplo de {} é {} e a raiz quadrada de {} é {:.2}'.format(n, d, n, t, n, rq))

