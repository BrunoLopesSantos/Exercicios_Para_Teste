soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
      soma += c
      cont += 1
# A soma acima e mesma da de baixo
#  cont = cont + 1
#  soma = soma + c
print('A soma de todos os {} valores solicitados e {}'.format(cont, soma))
