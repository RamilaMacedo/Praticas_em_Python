import math
an = float(input('Me diga um ângulo qualquer: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O valor do seno {:.3f}, cosseno {:.3f} e tangente {:.3f}'.format(sen, cos, tan))