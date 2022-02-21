real = float(input('Quanto de dinheiro voce tem na carteira ? R$'))
us = real / 5.20
usd = real / 6.14
print('com {}R$ voce pode compra {:.2f}=US$ e tambem ode compra {:.2f}=E$'. format(real, us, usd))