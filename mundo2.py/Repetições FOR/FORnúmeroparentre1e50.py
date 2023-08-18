"""
 Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""


for par in range(0, 50, 2):
#tbm pode ser feito assim,
#if par %(for divisivel) por 2 == 0:
    print(par, end=' ')

# é usado para iterar sobre uma sequência (lista, tupla, Dict, conjunto, str
# Executa um conjunto de instruções)

#PERCORRENDO UMA STRING

for i in 'Paralelepipedo':
    print(i)

#BREAK > poder de interrupção antes de chegar em todos os itens

l = ["pera", "caju", "bola", "cachorro"]
for i in l:
    #print(i)  print antes do break ele vai ate o pedido especificado em if
    if i == "bola":
        break
    print(i) #print após break ele terminar antes de chegar no item espeificado sem inclui-lo

l = ["sol", "mar", "lua", 24]
for i in l:
    #print(i)  
     if i == "mar":
        continue
    print(i) #nesse FOR ele pula o que foi especficado e da continuidade a lista apenas com o print após o continue,o print antes ele conta a lista toda

