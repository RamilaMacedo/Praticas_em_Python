'''numero = int(input('Digite um número: '))
num = str(numero)
print('Analisando esse número, temos:')
print('sua unidade é {}'.format(num[3]))
print('sua dezena é {}'.format(num[2]))
print('sua centena é {}'.format(num[1]))
print('seu milhar é {}'.format(num[0]))'''

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando esse número, temos:')
print('Sua unidade é {}'.format(u))
print('Sua dezena é {}'.format(d))
print('Sua centena é {}'.format(c))
print('Sua milhar é {}'.format(m))