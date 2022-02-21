peso = float(input('qual e o seu peso? (kg)'))
altura = float(input('qual e a sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa e de {:.1f}'.format(imc))
if imc < 18.5 :
    print('Voce esta ABAIXO do peso normal')
elif 18.5 <= imc < 25:
    print('PARABENS voce esta faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Voce esta em SOBREPESO')
elif 30 <= imc < 40:
    print('Cuidado voce esta em OBESIDADE')
elif imc >= 40:
    print('Cuidado voce esta em OBESIDADE MORBIDA')
