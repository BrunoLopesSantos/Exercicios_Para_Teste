time = ('Atletico MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'RB Bragantino',
        'Fluminense', 'America MG', 'Atletico GO', 'Santos', 'Ceara', 'Internacional',
        'São Paulo', 'Athletico PR', 'Cuiaba', 'juventude', 'Gremio', 'bahia', 'Sport',
        'Chapecoense')
print('=' * 150)
print(f'Lista Dos Time Do Brasileirão De 2021 {time}')
print('=' * 150)
print(f'Os 5 Primeros da Tabela Do Brasileirão São: {time[0:5]}')
print('=' * 150)
print(f'Os 4 Ultimos São :{time[-4:]}')
print('=' * 150)
print(f'Os Time Em Ordem Alfabetica {sorted(time)}')
print('=' * 150)
print(f'O Chapecoense Esta na Posição {time.index("Chapecoense")+1}')
'''for cont in range(19, len(time)):
    print(f'A {time[19]} Esta Na Posição {cont + 1}')'''
print('=' * 150)
