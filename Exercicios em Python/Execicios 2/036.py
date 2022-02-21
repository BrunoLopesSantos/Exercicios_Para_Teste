casa = float(input('\033[4;30mqual e o valor da casa: R$'))
sa = float(input('\033[4;30mqual e a sua renda mensal: R$'))
ano = int(input('\033[4;30mQuantos anos voce que pagar a parcela:'))
s1 = casa / (ano * 12)
s3 = sa * 30 / 100
print('\033[4;34mo valor da casa e {:.2f} e pagando em {} anos'.format(casa, ano), end=' ')
print('a parcela fica em {:.2f}'.format(s1))
if s3 >= s1:
    print('\033[4;32memprestimo aprovado')
elif s3 <= s1:
    print('\033[4;31memprestimo negado')
