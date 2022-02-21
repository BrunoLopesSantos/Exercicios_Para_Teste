cont = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro',
        'Cinco','Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze', 'Treze', 'Catorze',
        'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
        'Dezenove', 'Vinte')
while True:
    num = int(input('Digite Um Numeo De 0 A 20:'))
    if 0 <= num <= 20:
        break
    print('Tente Novamente. ', end='')
print(f'Voce Digitou O Numero {cont[num]}')
