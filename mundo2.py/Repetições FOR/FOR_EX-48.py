"""
Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

soma = 0
contador = 0
for n in range(1, 500):
    if n % 3 == 0:
        contador = contador + 1 # aqui ele informa a quantidade de números , soma 1
        soma = soma + n # aqui ele acumula números, acumula o valor
print('A soma de todos os resultados é', soma, 'e tem', contador, 'números')

