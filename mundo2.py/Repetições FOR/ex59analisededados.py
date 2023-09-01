"""
Digite o ano de nascimento de 7 pessoas .
Quantas pessoas não atigiram a maior idade
Quantas ja são maiores.
"""
from datetime import date

ano_atual = date.today().year #aqui estou trazendo o ano atual para descobrir la na frente a idade junto com a informação do ano de nascimento que a pessoa vai me dar
# > Fazendo um FOR irei incluir a quantidade de pessoas que quero saber no enunciado
# > Juntamente com a função Range() que percorre um conjunto de código um determinado nº de vezes
maioridade = 0
menoridade = 0
for people in range(1, 8):
    ano = int(input("Digite o ano do seu nascimento = "))

    idade = ano_atual - ano #subtraindo o ano de nascimento - ano atual vou saber a idade da pessoa

    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print("Temos {} maior de idade e {} menor de idade".format(maioridade, menoridade))

