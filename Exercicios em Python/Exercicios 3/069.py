tot18 = toth = totm20 = 0
while True:
    id = int(input('Idade :'))
    sx = ' '
    while sx not in 'MF':
        sx = str(input('Sexo [M/F] :')).strip().upper()[0]
    if id >= 18:
        tot18 += 1
    if sx == 'M':
        toth += 1
    if sx == 'F' and id < 20:
        totm20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]:')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Toatal de Pessoa Com Mais de 18 Anos e {tot18}')
print(f'Ao Todo Tem {toth} de Homes Cadastrados ')
print(f'E Temos {totm20} Mulheres Com Menos de 20 Anos')
