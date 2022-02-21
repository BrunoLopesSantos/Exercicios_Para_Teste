def titulo(txt):
    print(txt)
    print('-' * 30)
titulo('Controle De Terreno')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
s = l * c
def area(a, b, d):
    print(f'A Area De Um Terreno {a} x {b} é De {d}m')
 

area(l, c, s)