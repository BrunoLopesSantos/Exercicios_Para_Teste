valores = []
while True:
    n = int(input('Digite Um Numero :'))
    if n not in valores:
        valores.append(n)
    resp = str(input('Voce Quer Continuar [S/N]:'))
    if resp in 'Nn':
        break
print('-=-'*10)
print(f'Voce Digitou {len(valores)} Elementos')
valores.sort(reverse=True)
print(f'O Valor Em Ordem Decresente {valores}')
if n == 5:
    print('O Valor 5 Faz Parte Da Lista')
else:
    print('O Valor 5 Não Foi Encontrado Na Lista')