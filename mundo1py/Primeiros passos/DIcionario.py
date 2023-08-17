#tipo de mapeamento
#dict = dicionário
mydic = {
    "nome" : "ramila",
    "year" : 29,
    "altura" : 1.64
}
print(type(mydic))

#acesso a itens do dict

mydic = {
    "nome" : "ramila",
    "year" : 29,
    "altura" : 1.64
}
print(mydic["nome"])
x = mydic["altura"]
print(x)
z = mydic.get("year")
print(z)
#diferentes formas de acessar um item do dicionário
c = mydic.keys() #lista de chaves visualização do dicionário
c1 = mydic.values() #lista de valores
print(c,c1)

#ALTERANDO ITENS

mydic = {
    "nome" : "ramila",
    "year" : 29,
    "altura" : 1.64
}
mydic["nome"] = "Taissi" #trocando nome:ramila por nome:taissi
print(mydic)

mydic.update({"year": 40}) #atualiza o dicionário
print(mydic)


#ADICIONAR ITENS

mydic = {
    "nome" : "ramila",
    "year" : 29,
    "altura" : 1.64
}
mydic["sobrenome"] = "Macêdo" #adicionando item que não tem no dicionário
print(mydic)
mydic.update({"sobrenome": "Macêdo"})
print(mydic)

#REMOVER ITEM

mydic = {
    "nome" : "ramila",
    "year" : 29,
    "altura" : 1.64
}
mydic.pop("year") #método remove o item  com nome de chave especificado
print(mydic)
mydic.popitem() #remove o ultimo item da lista
print(mydic)
del mydic["year"] #a palavra chave del remove o item especificado
mydic.clear() #esvazia o dicionário
print(mydic)

#só a palavra chave "del" sem especificar vai deletar o dicionário inteiro


#DICIONÁRIO EM LOOP
#imprimir os itens (chave) do dicionário 1 por 1 
mydic = {
    "nome": "ramila",
    "year": 29,
    "apelido": "roms"
}
for i in mydic:
    print(i) #aqui ele imprimi só as chaves do dicionário
    print(mydic[i]) #aqui ele imprimi somente os values do dicionário
    
    #que tbm pode ser utilizado assim :
for i in mydic.values():
    print(i)

for x, y in mydic.items(): #vai imprimir todo o dicionário
    print(x, y)

#COPIAR DICIONÁRIO
#um dicionário não pode ser copiado simplesmente digitando dict2 = dict1 pq dict2 será apenas uma referÊncia a dict1
#existe várias maneiras de fazer uma cópia

#Método Copy()

mydic = {
    "profissao" : "Cientista de Dados",
    "curso" : "ADS",
    "ano-conclui" : 2024
}
x = mydic.copy() #método
x = dict(mydic) #função
#2 maneiras de copiar um dicionário
print(x)
