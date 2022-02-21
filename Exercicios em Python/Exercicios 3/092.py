from datetime import datetime 
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano De Nascimento: ')) 
dados['idade'] = datetime.now().year - nasc 
dados['ctps'] = int(input('Carterira de Trabalho (0 Não Tem): '))
if dados['ctps'] != 0: 
    dados['contratação'] = int(input('Ano Da Contratação: '))
    dados['salario'] = float(input('Salario: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 20)
print(dados)
for k, v in dados.items():
    print(f' -{k} Tem Valor {v}')