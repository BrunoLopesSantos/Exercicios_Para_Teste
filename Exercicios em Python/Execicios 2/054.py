from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 7):
    nasc = int(input('Em que ano a {} pesso nasceu ?'.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessos maiores de idade'.format(totmaior))
print('E tambem temos {} pessos menores de idade'.format(totmenor))
