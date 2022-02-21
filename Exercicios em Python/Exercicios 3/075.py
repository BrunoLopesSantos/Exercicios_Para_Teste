num = (int(input('Digite Um Numero :')),
       int(input('Digite Um Numero :')),
       int(input('Digite Um Numero :')),
       int(input('Digite Um Numero :')))
print(f'Voce Digitou Os Numeros : {num}')
print(f'O Valor 9 Aparaceu {num.count(9)} Vezes ')
if 3 in num:
    print(f'O Valor 3 Aparece Na {num.index(3) + 1} Posição')
else:
    print('O Valor 3 Não Foi Digitado Nenhuma Vez')
print('Os Valores Pares Digitados Foi ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
