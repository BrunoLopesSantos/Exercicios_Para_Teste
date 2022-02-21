from datetime import date
ano = int(input('qual e o seu ano :'))
atual = date.today().year
n1 = atual - ano
print('quem nasceu em {} tem {} anos'.format(ano, n1))
if n1 <= 9:
    print('E um atleta MIRIN')
elif n1 <= 14:
    print('E um atleta INFANTIL')
elif n1 <= 19:
    print('E um atleta JUNIOR')
elif n1 <= 25:
    print('E um atleta SENIOR')
#elif n1 > 25:
else:
    print('E um atleta MASTER')
