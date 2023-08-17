#Crie um programa que leia dois números e mostre a soma entre eles

x1 = float(input('digite um número:')) #float
print(x1)
x2 = float(input('digite mais um número:'))
print(x2)
soma = x1 + x2
print(' a soma desses dois números {} e {}  é{}'.format(x1, x2, soma))

print(x1 - x2) #subtração
print(x1 * x2) #multiplicação
print(x1 / x2) #divisão

#valor booleano são avaliados False quando: valores forem vazios
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool({})
bool([])

class myclass():
    def __len__(self):
        return 0
x = myclass()
print(bool(x)) #retornará falso

#x = 2j
x = -200
print(isinstance(x , int)) #isinstance é uma função interna outra maneira de retornar bool

