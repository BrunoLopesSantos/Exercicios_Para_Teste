"""import math"""
from math import sin, cos, tan, radians
angulo = float(input('qual e o Angulo ?'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O Angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O Angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O Angulo de {} tem a TANGETE de {:.2f}'.format(angulo, tangente))
