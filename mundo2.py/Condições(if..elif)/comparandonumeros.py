"""
Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem:

– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
"""

num = int(input('Me diga um número: '))
num1 = int(input('Me diga mais um número: '))
opção = num > num1
opção1 = num1 > num
if opção:
    print('O número {} é maior'.format(num))
    print('O \33[1;34mPRIMEIRO\33[m númro é maior')
elif opção1:
    print('O número {} é maior'.format(num1))
    print('O \33[1;31mSEGUNDO\33[m número é maior')
else:
    print('Os dois números são iguais')