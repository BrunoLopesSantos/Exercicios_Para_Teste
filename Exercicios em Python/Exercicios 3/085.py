numeros = [[], []]
n = 0
for c in range(1, 8):
    n = int(input(f'Digite o {c} Valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
        numeros[0].sort()
    else:
        numeros[1].append(n)
        numeros[1].sort()
print(f'Valores Pares Que Foram Digitados {numeros[0]} ')
print(f'Valores Impares Que Foram Digitados {numeros[1]}')
