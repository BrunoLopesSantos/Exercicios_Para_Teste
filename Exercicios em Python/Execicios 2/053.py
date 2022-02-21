frase = str(input('Digite uma frase :')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
# PODE-SE FAZER ASSIM TBM COM O FATIAMENTO
# inverso = junto [::-1]
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALINDROMO')
else:
    print('A frase digitada NAO E UM PALINDROMO')
