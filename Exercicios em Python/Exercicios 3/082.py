valores = []
while True:
    n = int(input('Digite Um Numero :'))
    if n not in valores:
        valores.append(n)
    resp = str(input('Voce Quer Continuar [S/N]:'))
    if resp in 'Nn':
        break
print(f'Lista Completa {valores}')
lista_par = []
lista_impar = []
for i in valores:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
print(f'Lista Dos Valores Pares {lista_par}')
print(f'Lista Dos Valores Impares {lista_impar}')
