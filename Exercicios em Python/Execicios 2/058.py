from random import randint
comp = randint(0, 10)
print('Sou seu computador... acabei de pensar em um numero de 0 a 10')
print('Voce consegui adivinha qual e ?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual e o seu palpite:'))
    palpite += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print('MAIS... Tente mais uma vez')
        elif jogador > comp:
            print('MENOS... Tente mais uma vez')
print('Acertou com {} tentativas'.format(palpite))

