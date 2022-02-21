n = int(input('digite um numero :'))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[30mO numero {} foi divisivel {} vezes'.format(n, t))
if t == 2:
    print('\033[32mO numero e PRIMO')
else:
    print('\033[33mO numero NAO E PRIMO')
