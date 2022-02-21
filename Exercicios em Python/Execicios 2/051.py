print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
ter = int(input('Primeiro termo:'))
ra = int(input('Razao:'))
decimo = ter + (10 - 1) * ra
for c in range(ter, decimo + ra, ra):
    print('{}'.format(c), end=' > ')
print('ACABOU')
