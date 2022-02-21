di = float(input('Qual e a distancia da viagem:'))
print('voce esta preste de começar uma vigem de {}Km.'.format(di))
# preço = di * 0.50 if di <= 200 else di * 0.45
if di <= 200:
    preço = di * 0.50
else:
    preço = di * 0.45
print('E o seu preço da viagem vai ser de {:.2f}R$'.format(preço))
