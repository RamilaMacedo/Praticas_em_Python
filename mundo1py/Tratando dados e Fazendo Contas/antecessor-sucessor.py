# > Um programa que leia um número inteiro e mostre na tela seu antecessor e seu sucessor

n = int(input('Digite um numero: '))
antecessor = n - 1
sucessor = n + 1
print('Tendo o número {} como base, vemos que seu antecessor é {} e seu sucessor é {}'.format(n, antecessor, sucessor))

n = int(input('digite um numero: '))
print('Tendo o numero {} como base, vemos que seu antecessor é {} e seu sucessor é {}'.format(n, (n-1),(n+1)))