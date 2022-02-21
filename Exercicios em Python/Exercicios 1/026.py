frase = str(input('fale uma frase:')).upper().strip()
print('A letra A aprece {} vezes'.format(frase.count('A')))
print('A letra A aprece na posiçao {}'.format(frase.find('A')+1))
print('A letra A apreceu pela ultima vez na posiçao {}'.format(frase.rfind('A')+1))