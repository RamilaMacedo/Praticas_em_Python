"""
 Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""


n = int(input('Digite um número para sua tabuada: '))
for t in range(1,11): #1 a 11 pq eu preciso da tabuada do 1 ao 10.
    print('{} x {} = {}'. format(n, t, n * t))


#OUTRA FORMA DE USAR O FOR

#tabuada utilizando FOR
n = int(input('Digite um número: '))
for t in range(1,11):
    num = n * t
    print(n, 'vezes', t, 'é igual a ', num)
