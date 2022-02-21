print('-=-'*11)
print('ANALISADOR DE TRIANGULOS')
print('-=-'*11)
r1 = float(input('primero seguimento:'))
r2 = float(input('segundo seguimento:'))
r3 = float(input('terçeiro seguimento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMA TRIANGULO',end=(' '))
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')

else:
    print('Os seguimentos acima NAO PODEM FORMA TRIANGULO')