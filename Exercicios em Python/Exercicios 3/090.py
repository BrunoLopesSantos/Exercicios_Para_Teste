dados = {}
dados['nome'] = str(input('Qual e o Seu Nome:'))
dados['media'] = float(input(f'A Media de {dados["nome"]} é:'))
print(f'nome e Igual a {dados["nome"]}')
print(f'A Media e Igual {dados["media"]}')
if dados['media'] >= 6:
    print('Situação e Igual Aprovado')
else:
    print('Situação e Igual Reprovado')
print(dados)