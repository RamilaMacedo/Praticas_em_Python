"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
"""  

  #centralizar
print('{:*^20}'.format('ROMS'))

#Grenciador de pagamento
produto = float(input('Qual valor do seu produto: R$'))
print('''Formas de pagamento  
[1] para a vista no dinheiro ou no cheque
[2] para cartão a vista
[3] para ate 2 x no cartão
[4] para parcelas de 3x ou mais''') #as 3 aspas no inicio e no fim vc pode usar várias linhas
pgmt = int(input('Escolha sua opção de pagamento? '))

#codição de pagamento
if pgmt == 1:
    total = produto - (produto * 10/100)
elif pgmt == 2:
    total = produto - (produto * 5/100)
elif pgmt == 3:
    total = produto
    parcela = total / 2
    print('Sua compra será parceladas em 2x de R$ %.2f ' % parcela )
elif pgmt == 4:
    total = produto + (produto * 20 / 100)
    parcelas = int(input('Quantas parcelas deseja comprar? '))
    totparc = total / parcelas
    print('Sua compra será parcelada em {}x de R$ {:.2f}'.format(parcelas, totparc))
print('Sua compra custará R$ %.2f' % total)



