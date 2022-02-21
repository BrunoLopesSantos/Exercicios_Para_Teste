valor = list()
for cont in range(0, 5):
    valor.append(int(input(f'Digite Um Valor Para Posição {cont}:')))
    if cont == 0:
        mai = men = valor[cont]
    else:
        if valor[cont] > mai:
            mai = valor[cont]
        if valor[cont] < men:
            men = valor[cont]
print('-=-'*25)
print(f'Voce Digitou Os Valor {valor}')
print(f'O Maior Valor Digitado Foi {mai} Nas Posições ', end='')
for i, v in enumerate(valor):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O Menor Valor Digitado Foi {men} Nas Posições ', end='')
for i, v in enumerate(valor):
    if v == men:
        print(f'{i}...', end='')
print()
