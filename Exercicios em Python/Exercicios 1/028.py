
import random
from time import sleep
print('\033[7;30m-=-' *13)
print('\033[7;30mVOU PENSAR EM UM NUMERO DE 0 A 5')
print('-=-' *13)
n1 = int(input('\033[4;30;44mem que numero eu pensei ?'))
num = random.randint(0, 5)
print('\033[7;30mProcessando.....')
sleep(3)
if n1 == num:
    print('*' *35)
    print('\033[30;42m**** Parabens voce acertou ****')
    print('*' *35)
else:
    print('¨' *53)
    print('\033[30;41mERRROOOUUU, Eu Ganhei! voce escolheu {} eu pensei em {} '.format(n1, num))
    print('¨' *53)

print('====== FIM =======')