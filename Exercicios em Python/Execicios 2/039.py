from datetime import date
from time import sleep
'''s = int(input('\033[4;30mqual e o seu genero\n[1] masculino \n[2] feminino\nescolha:'))
if s == 1:
    print('\033[4;30mContinuando...')
    sleep(3)
else:
    print('voce nao precisa se alistar')'''
# tenho que arrumar ainda
ano = int(input('qual ano voce nasceu:'))
atual = date.today().year
n1 = atual - ano
n2 = 18 - n1
n3 = n1 - 18
n = n2 + atual
nn = atual - n3
if n1 < 18:
    print('\033[4;32mAinda falta {} anos pra voce-se alistar'.format(n2))
    print('\033[4;32mvoce se alistara em {}'.format(n))
elif n1 == 18:
    print('\033[4;30;41mVoce prcisa se alistar esse ano')
elif n1 > 18:
    print('\033[4;34mo cara que nasceu em {} tem {} anos em {}'.format(ano, n1, atual))
    print('\033[4;34mVoce deveria ter se alistado ha {} anos'.format(n3))
    print('\033[4;34mVoce se alisto em {}'.format(nn))
