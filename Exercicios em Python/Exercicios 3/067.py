n = 0
while True:
    n = int(input('Digite um Numero Para Ver a Tabuada:'))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c :2} = {n * c}')

print('fim')
