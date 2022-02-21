
time = []
dadosfut = {}
lis_ta = [] 
while True:
    dadosfut.clear()
    dadosfut['nome'] = str(input('Nome Do Jogador: '))
    jogos = int(input(f'Quantas Partidas {dadosfut["nome"]} Jogou: '))
    lis_ta.clear()
    for c in range(0, jogos):
        lis_ta.append(int(input(f'Quantos GOSl Foram Feitos No Jogo {c}: ')))
    dadosfut['gosl'] = lis_ta
    dadosfut['total'] = sum(lis_ta)
    time.append(dadosfut.copy())
    while True:
        resp = str(input('Voce quer Continua [S/N]:')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por Favor, Digite Apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for c in dadosfut.keys():
    print(f'{c:<15}', end='')
print()
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for c in v.values():
        print(f'{str(c):>15}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar Dados De Qual Joogador ? (999 Para Parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não Existe Jogador Com Codigo {busca}')
    else:
        print(f' LEVANTAMENTO DO JOGADOR {time[busca]["gosl"]}:')
        for i, g in enumerate(time[busca]['gosl']):
            print(f'    No jogo {i+1} Fez {g} Gosl.')
    print('-=' * 30)
print('<<< VOLTE SEMPRE >>>')   
# TEM QUE REVER