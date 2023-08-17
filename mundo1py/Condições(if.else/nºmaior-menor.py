"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

n1 = input('Digite um número:')
n2 = input('Digite mais um número:')
n3 = input('Digite o terceiro número: ')
if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O maior número é:{}'.format(maior))
if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('O menor número é:{}'.format(menor))
