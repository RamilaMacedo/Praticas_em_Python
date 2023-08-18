"""
Faça um programa que leia um nº inteiro e diga se ele é ou não um nº primo
"""
# Um número primo só é divisivel por 1 e por ele mesmo

num = int(input(" Digite um nº: "))

tot = 0
for c in range(1, num +1):
    if num % c == 0: #se um numero for dividivel pelo contador(c)
        print("\33[34m", end=" ") #aqui mostra qual números são divisíveis
        tot += 1
    else:
        print("\33[32m", end=" ") #aqui mostra qual número não foi divisível pelo número digitado
    print("{}".format(c), end=" ") #O espaço entre os número que sairão na tela se da pelo end=" "
print("\n\033[m O número {} foi divisível {} vezes".format(num, tot))
#>\033 vai zerar a cor que foi colocar la em cima na hora que mostrar no terminal
if tot == 2:
    print('Por isso ele é Primo!')
else:
    print('Ele não é Primo')