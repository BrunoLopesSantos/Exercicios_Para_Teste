num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for c in range(0, 3):
    for v in range(0, 3):
        num[c][v] = int(input(f'Digite Um Valor Para {c}, {v}:'))
print('-=' * 30)
for c in range(0, 3):
    for v in range(0, 3):
        print(f'[{num[c][v]:^5}]', end='')
        if num[c][v] % 2 == 0:
            spar += num[c][v]
    print()
print('-=' * 30)
print(f'A Soma Dos Numeros Pares é {spar}')
for c in range(0, 3):
    scol += num[c][2]
print(f'A Soma Dos Valores Da Terceira Coluna é {scol}')
for v in range(0, 3):
    if v == 0:
        mai = num[1][v]
    elif num[1][v] > mai:
        mai = num[1][v]
print(f'O Maior Valor Da Segunda Linha é {mai}')