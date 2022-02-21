nu = float(input('qual e a velocidade do carro?'))
if nu > 80:
    print('MULTADO! Voce excedeu o limete permitido que e de 80Km/h')
    multa = (nu -80) * 7
    print('Sua multa fica {}R$'.format(multa))
print('Tem um bom dia! dirija em segurança')


