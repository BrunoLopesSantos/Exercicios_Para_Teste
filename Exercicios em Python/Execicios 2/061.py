print('Gerador de PA')
print('=' * 15)
primero = int(input('Primero termo:'))
razao = int(input('Razao ds PA:'))
termo = primero
cont = 1
while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')