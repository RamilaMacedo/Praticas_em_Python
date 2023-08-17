#Faça um programa que leia algo pelo teclado 
#Mostre seu tipo primitivo 
#E todas as informações possíveis

x1 = (input('digite algo: '))

print('O tipo primitivo é', type(x1))

print('Ele é alfanumerico?', x1.isalnum())
print('Ele contem apenas letras?', x1.isalpha())
print('Ele é um número?', x1.isnumeric())
print('Ele é um decimal', x1.isdecimal())
print('Todos os caracteres são caracteres?', x1.isascii())
print('Todos os caracteres são digitos?', x1.isdigit())
print('Temos letras minúsculas?', x1.islower())
print('Todos os caracteres são espaços em branco?', x1.isspace())
print('Temos letras em caixa alta?', x1.isupper())

#  > Mais alguns métodos de strings
#capitalize() #converte o 1º caracter em maiúscula
txt = "eu gosto de praia"
x = txt.capitalize()
print(x)

#casefold() #converte strings em letras minúsculas
txt = "Eu Gosto De Praia"
x = txt.casefold()
print(x)

#center() #retorna uma string centralizada, especificando os espaços de caracteres
txt = "eu gosto de praia"
x = txt.center(20)
print(x)

#count() #retorna o nº de vezes que um valor especificado ocorre em uma string
txt = "eu gosto de praia"
x = txt.count("a")
print(x)

#encode() #retorna uma versão codificada da string
txt = "eu gosto de praia"
x = txt.encode()
print(x)

#endswith() #retorna TRUE se a string terminar com valor espcificado
txt = "eu gosto de praia"
x = txt.endswith("praia")
print(x)

#find()/index() > Procura na string um valor especificado e retorna a posição de onde foi encontrado
txt = "eu gosto de praia"
x = txt.index("praia")
print(x)

#format() > Formata os valores especificados em uma string
txt = "eu gosto de praia"
print(txt.format())

#isidentifier() > Retorna True se a string for um identificador
#para ser um identificador tem que conter (a-z),(0-9),(_) não pode ter espaços
txt = "eu_gosto_de_praia"
print(txt.isidentifier()) 

#lstrip() > Retorna uma versão de corte à esquerda da string
txt = "eu_gosto_de_praia"
x = txt.lstrip()
print("sol", x , "futevolei")

#Para mais exemplos de tipos tem uma lista no site w3schools.com