"""pessoas = list()
dados = list()
mai = men = 0
while True:
    pessoas.append(str(input('Nome :')))
    pessoas.append(float(input('Peso :')))

    if len(dados) == 0:
        mai = men = dados
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    dados.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Voce Quer Continuar [S/N]: '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao Todo Voce Cadastrou {len(dados)} Pessoas')
print(f'O Maior Peso Foi {mai}.0Kg Peso De ', end='')
for p in dados:
    if p[1] == mai:
        print(f'{p[0]}', end='')
print()
print(f'O menor Peso Foi {men}.0Kg Peso De ', end='')
for p in dados:
    if p[1] == men:
        print(f'{p[0]}', end='')
print()"""
# TENHO QUE REVISAR ESSE
# TA DANDO ERRO NA LINHA 11