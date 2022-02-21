total = totmil = menor = cont = 0
barato = ''
while True:
    prod = str(input('Qual e o Produto:'))
    preço = int(input('Preço R$:'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = prod
# pode cimplifica
#    else:
#        if preço < menor:
#           menor = preço
#            barato = prod
# Mais Funciona Nos Dois Casos
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O Total da Compra Foi R${total:.2f}')
print(f'Temos {totmil} um Produto Custando R$ 1000.00')
print(f'O Produto Mais Barato Foi {barato},E o Preço Foi de R${menor:.2f}')
