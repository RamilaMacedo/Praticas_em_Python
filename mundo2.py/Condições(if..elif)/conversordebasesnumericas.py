"""
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""

numero = int(input('Escreva um numero: '))
print('''Escolha qual será a base de conversão:
[1] para base Binário
[2] para base Hexadecimal
[3] para base Octal''')
opção = int(input('O que você escolhe: '))
if opção == 1:
    print('{} convertido em binário é {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('{} convertido em hexadecimal é {}'.format(numero, hex(numero)[2:]))
elif opção == 3:
    print('{} convertido em octal é {}'.format(numero, oct(numero)[2:]))
else:
    print('Opção inválida')

