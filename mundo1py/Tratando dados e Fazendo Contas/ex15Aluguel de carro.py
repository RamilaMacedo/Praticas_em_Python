km = float(input('Quantos quilômetro foi percorrido: '))
dias = int(input('Quantos dias o carro foi alugado: '))
print('o carro custa R$60')
print('valor em km rodado custa R$0,15')
print('-' * 20)
p1a = dias * 60
p2km = km * 0.15
print('Foi pago pelo carro R${:.2f} relacionado a {} dias alugados e R${:.2f} de gasolina por km rodados.'.format(p1a, dias, p2km))
total = p1a + p2km
print('Num total de R${:.2f}.'.format(total))