"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

soma = 0
contador = 0
for c in range(1,7):
    n = int(input('Digite {}º número: '.format(c)))
    if n % 2 == 0:
        soma += n
        contador += 1
print('Temos {} números PARES a soma deles é igual a {}'.format(contador, soma))

