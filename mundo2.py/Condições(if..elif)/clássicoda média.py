"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
"""

nota = float(input('Primeira Nota: '))
nota1 = float(input('Segunda Nota: '))
m = nota + nota1 / 2
print('Sua Média foi {}'.format(m))

if m < 5:
    print('\33[1;31mREPROVADO\33[m')
elif m > 5 and m <= 6.9:
    print('\33[1;33mRECUPERAÇÃO\33[m')
else:
    print('\33[1;32mAPROVADO\33[m')