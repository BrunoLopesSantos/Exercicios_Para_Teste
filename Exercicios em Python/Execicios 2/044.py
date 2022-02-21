print('{:=^40}'.format(' LOJA TRANSMARK '))
valor = float(input('Preço das compra R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opçao = int(input('Qual e a opção :'))
if opçao == 1:
    total = valor - (valor * 10 / 100)
elif opçao == 2:
    total = valor - (valor * 5 / 100)
elif opçao == 3:
    total = valor
    parcela = total / 2
    print('Seu valor sera parcelado em 2x de R${}'.format(parcela))
elif opçao == 4:
    total = valor + (valor * 20 / 100)
    tp = int(input('Quantas parcela?'))
    parcela = total / tp
    print('Sua compra sera parcelada {}x de R${:.2f} COM JUROS'.format(tp, parcela))
else:
    total = 0
    print('OPÇÃO INVALIDA tente novamente')
print('Sua compra de R${:.2f} vai custa R${:.2f} no final'.format(valor, total))