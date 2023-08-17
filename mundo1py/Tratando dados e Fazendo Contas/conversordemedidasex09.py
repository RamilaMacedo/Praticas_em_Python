# > Um programa que leia um valor em metros e o exiba convertendo em cm e mm

m = float(input('Digite um valor em metros:'))
km = m * 0.001
hec = m * 0.01
dec = m * 0.1
dem = m * 10
cm = m * 100
mm = m * 1000
print('Quilometro  equivale a : {:.3f}'.format(km))
print('Hectometro equivale: {}'.format(hec))
print('Decametro equivale: {}'.format(dec))
print('Decimentro equivale: {}'.format(dem))
print('Centimetro equivale: {}'.format(cm))
print('Milímetrom equivale: {}'.format(mm))