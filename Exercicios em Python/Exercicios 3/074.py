from random import randint
valores = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os Valores Que Foram Sortiados : ', end='')
for n in valores:
    print(f'{n}', end=' ')
print(f'\nO Maior Valor Sortiado Foi {max(valores)}')
print(f'O Menor Valor Sortiado Foi {min(valores)} ')