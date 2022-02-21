sexo = str(input('Imforme o seu sexo:[M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('dados invalidos. por favor, digite novamente:')).strip().upper()
print('sexo {} registrado com sucesso'.format(sexo))