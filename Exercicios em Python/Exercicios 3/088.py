from random import randint
from time import sleep
li_ta = list()
jogos = list()
print('-=' * 30)
print('       JOGA NA MEGA SENA       ')
print('-=' * 30)
jog = int(input('Quantos Jogos Voce Quer Que Eu Sorteie?:'))
tot = 1
while tot <= jog:
    cont = 0
    while True:
     num = randint(1, 60)
     if num not in li_ta:
         li_ta.append(num)
         cont += 1
     if cont >= 6:
        break
    li_ta.sort()
    jogos.append(li_ta[:])
    li_ta.clear()
    tot += 1
print('-=' * 3, f'  SORTEANDO {jog} JOGOS  ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '  BOA SORTE  ', '-=' * 5)