produto = float(input('Valor do produto a ser vendida: R$ '))
print('-'*20)
print('desconto de 5% no produto')
desconto = produto * 0.05
pd = produto - desconto
print('O produto com valor R${:.2f} ficará por R${:.2f} com desconto de 5%.'.format(produto,pd))

salário = float(input('Valor do salário de um funcionário: R$ '))
print('aumento de 15% no salário')
aumento = salário + (salário * 15 / 100)

print(' Com o aumento de 15%, Râmila passou a ganhar R${:.3f}'.format(aumento))

salário = float(input('Valor do salário de um funcionário: R$ '))
print('aumento de 15% no salário')
aumento = salário * 0.15
ns = salário + aumento
print(' Com o aumento de 15%, Râmila passou a ganhar R${:.3f}'.format(ns))
