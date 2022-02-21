num = cont = soma = 0
num = int(input('Digite Um Numero [999 para parar]:'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite Um Numero [999 para parar]:'))
print('Voce Dititou {} Numeros, e a Soma Entre Eles Foi {} '.format(cont, soma))
