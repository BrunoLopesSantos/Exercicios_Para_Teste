from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
com = randint(0, 2)
print('''SUAS OPÇÕES 
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jo = int(input('Qual e a sua jogada :'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-'* 11)
print('O computador jogou {}'.format(itens[com]))
print('O jogador jogou {}'.format(itens[jo]))
print('-=-'* 11)
if com == 0:
    if jo == 0:
        print('EMPATE')
    elif jo == 1:
        print('JOGADOR VENCE')
    elif jo == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGA INVALIDA')

elif com == 1:
    if jo == 0:
        print('COMPUTADOR VENCE')
    elif jo == 1:
        print('EMPATE')
    elif jo == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGA INVALIDA')

elif com == 2:
    if jo == 0:
        print('JOGADOR VENCE')
    elif jo == 1:
        print('COMPUTADOR VENCE')
    elif jo == 2:
        print('EMPATE')
    else:
        print('JOGA INVALIDA')

