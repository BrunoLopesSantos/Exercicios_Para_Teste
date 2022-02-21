salario = float(input('qaul e o seu salario? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcinario que ganhava R${:.2f}, com o aumento de 15%, passa a ganhar R${:.2f}'.format(salario, novo))
