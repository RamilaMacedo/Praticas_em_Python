"""
Programa que ler o peso de 5 pessoas.
Mostrar qual maior e o menor peso lidos
"""

maior = 0   
menor = 0
for p in range(1, 6): #quero ler o peso de 5 pessoas por isso de 1 a 6
    peso = float(input(f"Peso da {p} pessoa: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso é {maior}")
print(f"O menor peso é o {menor}")