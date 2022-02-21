'''co = float(input(' qual e o cateto osposto '))
ca = float(input(' qual e o cateto adijcente'))
ip = (co ** 2 + ca ** 2) ** (1/2)
print('o valor da ipotenusa e {:.2f}'.format(ip))'''

'''import math'''
from math import hypot
co = float(input('qaul o valor do cateto oposto'))
ca = float(input('qual o valor do cateto adjcente'))
hi = hypot(co, ca)
print('o valor da ipotenusa e {:.2f}'.format(hi))


