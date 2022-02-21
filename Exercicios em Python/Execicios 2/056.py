si = 0
mdi = 0
mdih = 0
hm = ''
totm20 = 0
for p in range(1, 5):
    print('---- {} pessoa ----'.format(p))
    nome = str(input('nome :'))
    idade = int(input('idade :'))
    sexo = str(input('sexo [M/F]:')).strip()
    si += idade
    if p == 1 and sexo in 'Mm':
        mdih = idade
        hm = nome
    if sexo in 'Mm' and idade > mdih:
        mdih = idade
        hm = nome
    if sexo in 'Ff' and idade < 20:
        totm20 += 1
mdi = si / 4
print('A media de idade do grupo e {}'.format(mdi))
print('O homen mais velho tem {} anos e se chama {}'.format(mdih, hm))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totm20))
