"""
Desenvolva um programa que leia o 1º termo e a razão de uma PA.
Mostre os 10 primeiros termos dessa PA
"""
# O que é uma Progressão Aritmética
"""
>> Sequencia numérica que serve para descrever eventos da matemática 
* crescente ou;
* descrescente;
(sendo sempre constante) = a diferença sempre será a mesma e essa diferença da-se o nome de RAZÃO
"""

# Para identificar uma PA precisamos saber seu primeiro termo e a razão
primeiro_termo = int(input(" 1º Termo: "))
razao = int(input(" Razão: "))
# > Formula Matemática da PA = an = a1 + (n-1) * r
"""
n é a posição do termo
a1 é o 1º termo
r é a razão
"""

decimo_termo = primeiro_termo + (10-1) * razao

for pa in range(primeiro_termo, decimo_termo + razao, razao):
    print("{}".format(pa), end="->")
print("fim")