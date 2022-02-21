print('GERADOR DE PA')
print('=' * 15)
primero = int(input('Primeiro termo:'))
razao = int(input('Razao:'))
termo = primero
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} >'.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos Termos Voce Que Mostrar a Mais?'))
print('Fim Da Progressao, Foi Finalisado Com {} Termos '.format(total))
