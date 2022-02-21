num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in range(0, 3):
    for v in range(0, 3):
        num[c][v] = int(input(f'Digite Um Valor Para {c}, {v}:'))
print('-=' * 30)
for c in range(0, 3):
    for v in range(0, 3):
        print(f'[{num[c][v]:^5}]', end='')
    print()
