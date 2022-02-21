#pode ser feito assim
#from math import factorial
'''n = int(input('Digite um numero para ver fatorial:'))
f = factorial(n)
print('O fatoride de {} é {}'.format(n, f))'''
#Agora o jeito mais longo
n = int(input('Digite um Numero para ver o Fatorial:'))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x 'if  c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
