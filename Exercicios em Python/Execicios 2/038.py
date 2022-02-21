n1 = int(input('\033[4;30mPrimero numero :'))
n2 = int(input('\033[4;30mSegundo numero :'))
if n1>n2:
    print('\033[4;32mO primeiro numero e o maior')
elif n2>n1:
    print('\033[4;32mO segundo numero e o maior')
else:
    print('\033[4;32mNao existe valor maior, os dois sao iguais')
