valores = []
while True:
    n = (int(input('Digite Um Numero :')))
    if n not in valores:
        valores.append(n)
        print('Valor Adicionado Com Sucessso......')
    else:
        print('Valor Duplicado! Não Foi Adicionado......')
    resp = str(input('Voce quer Continua [S/N]:')).strip().upper()[0]
    if resp in 'Nn':
        break
print('-=-'*13)
valores.sort()
print(f'Voce Digito Os Valores {valores}')

