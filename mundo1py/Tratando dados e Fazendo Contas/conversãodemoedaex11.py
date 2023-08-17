# >Um programa que leia quanto de dinheiro a pessoa tem na carteira 
# >Mostre quanto pode comprar em dólares e Euro

real = float(input('Quantos reais você tem na carteira? R$'))
dolar = real / 5.64
euro = real / 6.52
print('Com R${} você pode comprar US${:.2f} e EUR{:.2f}'.format(real, dolar, euro))