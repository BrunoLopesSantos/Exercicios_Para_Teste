from time import sleep
n1 = int(input('digite o primero valor :'))
n2 = int(input('digite o segundo valor :'))
opçao = 0
while opçao != 5:
    print('''    [1] somar
    [2] mutiplicar
    [3] maior
    [4] novos numero
    [5] sair do progama''')
    opçao = int(input('>>>>>>>qual e a sua opçao:'))
    if opçao == 1:
        soma = n1 + n2
        print('A soma de entre {} + {} é {}'.format(n1, n2, soma))
    elif opçao == 2:
        prod = n1 * n2
        print('O Resultado de {} x {} é {}'.format(n1, n2, prod))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} O maior e {}'.format(n1, n2, maior))
    elif opçao == 4:
        print('Informe os valores novamente')
        n1 = int(input('Digite o Primero Valor:'))
        n2 = int(input('Digite o Segundo Valor:'))
    elif opçao == 5:
        print('FINALIZANDO.......')
    else:
        print('opçao invalida tente novamente')
    print('=*='*10)
    sleep(2)
print('FIM do PROGAMA! Volte Sempre')