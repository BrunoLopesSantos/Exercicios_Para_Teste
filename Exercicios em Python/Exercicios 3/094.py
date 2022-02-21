dados = []
pes = {}
soma = mdi = 0
while True:
    pes.clear
    pes['nome'] = str(input('Nome: '))
    while True:   
        pes['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pes['sexo'] in 'MF':
            break
        print('ERRO! Por Favor, Digite Apenas M ou F')
    pes['idade'] = int(input('Idade: '))
    soma += pes['idade']
    dados.append(pes.copy())
    while True:
        resp = str(input('Voce quer Continua [S/N]:')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por Favor, Digite Apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print(dados)
print('-=' * 30)
print(f'A) Ao Todo Temos {len(dados)} Pessoas Cadastradas')
mdi = soma / len(dados)
print(f'B) A Media De Idade é {mdi:5.2f} Anos')
print(f'C) As Mulheres Cadastradas Foram ', end='')
for c in dados:
    if c["sexo"] == 'F':
        print(f'{c["nome"]} ', end='')
print('')
print('D) A Lista De Pessoas Que Estão Acima Da Media: ')
for v in dados:
    if v["idade"] >= mdi:
        print('   ', end='')
        for c, k in v.items():
            print(f'{c} = {k};', end='')
        print()
print('<<< ENCERRADO >>>')