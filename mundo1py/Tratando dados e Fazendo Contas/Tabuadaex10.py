#ler um número inteiro e mostrar sua tabuada

n = int(input('Digite um número: '))
print('Segue Tabuada de {}{}{}'.format('\33[4;34m', n, '\33[m'))
print('\33[1;31m-\33[m' * 20)
print('{} - 1 = {}'.format(n,n-1))
print('{} - 2 = {}'.format(n,n-2))
print('{} - 3 = {}'.format(n,n-3))
print('{} - 4 = {}'.format(n,n-4))
print('{} - 5 = {}'.format(n,n-5))
print('{} - 6 = {}'.format(n,n-6))
print('\33[1;31m-\33[m' * 20)