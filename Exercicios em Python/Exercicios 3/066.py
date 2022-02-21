cont = soma = 0
while True:
    n = int(input('Digite um Numero[Se Quiser Para o Progama Digite 999]:'))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Voce Digitou {cont} numeros, E soma dos valores e {soma}')