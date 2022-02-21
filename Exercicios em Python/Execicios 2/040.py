n1 = float(input('\033[4;30mprimera nota:'))
n2 = float(input('\033[4;30msegunda nota:'))
n3 = (n1 + n2) / 2
print('tirando {} e {} a media e {:.2f}'.format(n1, n2, n3))
if n3 < 5.0:
    print('\033[4;31mREPROVADO')
elif 7> n3 > 5:
    print('\033[4;34mVoce esta de RECUPERAÇAO')
elif n3 > 7.0:
    print('\033[4;32mAPROVADO')
