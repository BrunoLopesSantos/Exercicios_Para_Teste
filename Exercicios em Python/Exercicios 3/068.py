from random import randint
v = 0
while True:
    n = int(input('Digite um Numero:'))
    comp = randint(0, 10)
    soma = n + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I] ?')).strip().upper()[0]
    print(f'Voce Jogou {n} e o Computador Jogou {comp} A Soma deu {soma}', end=' ')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('VOCE VENCEU')
            v += 1
        else:
            print('VOCE PERDEU')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('VOCE VENCEU')
            v += 1
        else:
            print('VOCE PERDEU')
            break
    print('Vamos Joga Novamente.......')
print(f'GAME OVER!!! Voce Ganhou {v} Vezes ')
