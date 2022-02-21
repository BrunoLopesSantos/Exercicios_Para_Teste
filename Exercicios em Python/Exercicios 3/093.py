dadosfut = {}
lis_ta = []
# tot = 0 
dadosfut['nome'] = str(input('Nome Do Jogador: '))
jogos = int(input(f'Quantas Partidas {dadosfut["nome"]} Jogou: '))
for c in range(jogos):
    go = int(input(f'Quantos GOSl Foram Feitos No Jogo {c}: '))
#    tot += go
    lis_ta.append(go) 
    dadosfut['gosl'] = lis_ta
    dadosfut['total'] = sum(lis_ta)
#  dadosfut['total'] = tot
print('-=' * 30)    
print(dadosfut)
print('-=' * 30)
for c, v in dadosfut.items():
    print(f'O Campo {c} Tem o Valor {v}')
print('-=' * 30)
print(f'O Jogador {dadosfut["nome"]} Jogou {len(dadosfut["gosl"])} Partidas')
for v, c in enumerate(dadosfut['gosl']):
     print(f'  => Na Partida {v}, Fez {c} GOSl')
print(f'Foi Um Total De {dadosfut["total"]} GOSl')