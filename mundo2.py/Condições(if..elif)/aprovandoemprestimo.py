"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

casa = float(input('Qual o valor da casa? R$ '))
salário = float(input('Qual salário do comprador? R$ '))
anos = int(input('Em quantos anos ele pretende pagar a casa? '))
p = casa / (anos * 12)
mínimo = salário * 30/100
print('Com o valor da casa em R$ {} vc terá que pagar as prestações de R${} durante {} anos'.format(casa, mínimo, anos))
if p <= mínimo:
    print(' O empréstimo séra APROVADO')
else:
    print(' O empréstimo será {}NEGADO'.format('\33[31m','\33[m'))
