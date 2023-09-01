"""
Cria um detector de Palíndromo - desconsiderar espaços
ex:
(APOS A SOPA/ A SACADA DA CASA/ A TORRE DA DERROTA/ O LOBO AMA O BOLO/ ANOTARAM A DATA DA MARATONA)
"""
# > O que seria um Palíndromo? < Vocábulo que se lê da mesma forma de trás para frente>


frase = input("Digite uma frase: ").strip().upper()
#strip = é um método em python que remove espaços em branco iniciais e finais
#upper = retorna uma string para todos os caracteres MAIÚSCULO, nesse caso, usamos para não causar dúvida ao digitar a frase , pois poderá retornar um erro , mesmo a frase sendo um palíndromo
palavras = frase.split()
#split = divide uma string em uma lista
# > Após dividir a string em um lista , dai consigo fazer a junção de toda a string usando join
juntar = "".join(palavras)
print(juntar)
inverso = "" #só irá funcionar quando eu chamar dentro do For
for p in range(len(juntar)-1, -1, -1):
    inverso += juntar[p]
if inverso == juntar:
    print('É um palíndromo')
else:
    print(f"Não é palíndromo, ela se escreve assim",inverso)
# len: é uma função que retorna o número de itens dentro do objeto

"""
temos outra forma de fazer sem usar o FOR
segue: 
"""
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = juntar[::-1]
print(inverso)
if inverso == juntar:
    print('Temos um palíndromo')
else:
    print('Isso não é um Palíndromo')