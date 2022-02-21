nu = int(input('digite um numero'))
print('''Escolha uma conversao:
[ 1 ] converte pára BINARIO
[ 2 ] converte para OCTAL
[ 3 ] converte para HEXADECIMAL''')
opçao = int(input('escolha sua opçao:'))
if opçao == 1 :
    print('{} convertido para BINARIO e igual {}'.format(nu, bin(nu)[2:]))
elif opçao == 2:
    print('{} convertido para OCTAL e igual {}'.format(nu, oct(nu)[2:]))
elif opçao == 3:
    print('{} convertido em HEXSDECIMAL e igual a {}'.format(nu, hex(nu)[2:]))
else:
    print('Opçao invalida, Tenti novamente')

