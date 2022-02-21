s = float(input('qual e o seu salario: '))
if s <= 1250.00:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 / 100)
print('quem ganhva {:.2f}R$ agora passa a ganhar {:.2f}R$'.format(s, novo))