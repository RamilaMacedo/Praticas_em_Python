"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Qual seu salário? R$'))
if salario <= 1.250:
    novo = salario + (salario * 10 / 100)
    print('Seu salário com aumento de 10% fica R${:.2f}'.format(novo))
else:
    novo1 = salario + (salario * 15 / 100)
    print('Seu salário com aumento de 15% fica R${:.2f}'.format(novo1))
