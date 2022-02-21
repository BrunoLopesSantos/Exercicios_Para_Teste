from datetime import date
ano = int(input('qual o ano voce analisar? se quiser analisar o ano atual digite 0 :'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} e Bissexto'.format(ano))
else:
    print('O ano {} Nao e Bissexto'.format(ano))
