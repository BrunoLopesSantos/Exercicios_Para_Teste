resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um Numero:'))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer Continuar [S/N]:')).upper().strip()
media = soma / quant
print('Voce Digitou {} Numero, e a Media Foi {}'.format(quant, media))
print('O Maior Numero Foi {}, E O Menor Numero Foi {}'.format(maior, menor))