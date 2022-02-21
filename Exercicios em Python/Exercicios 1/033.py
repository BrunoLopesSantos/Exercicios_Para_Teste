a = int(input('primeiro valo:'))
b = int(input('segundo valor:'))
c = int(input('terciro valor:'))
menor = a
# verificando quem e o menor
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando quem e o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o menor valor foi {}'.format(menor))
print('o maior valor foi {}'.format(maior))



