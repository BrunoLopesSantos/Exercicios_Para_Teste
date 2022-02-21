from random import randint
from time import sleep
from operator import itemgetter
jog = {'jogador1':randint(1, 6), 'jogador2':randint(1, 6),
 'jogador3':randint(1, 6), 'jogador4':randint(1, 6)}
rank = list()
for k, v in jog.items():
    print(f'   O {k} Tirou {v} No jogo')
    sleep(1)
rank = sorted(jog.items(), key=itemgetter(1), reverse=True)
print('==== Ranking Dos Jogadores ====')
for i, v in enumerate(rank):
    print(f'   O {i+1}° Lugar: {v[0]} com {v[1]}. ')
    sleep(1)