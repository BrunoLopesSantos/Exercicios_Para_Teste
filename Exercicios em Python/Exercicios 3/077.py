palavras = ('Aprender', 'Gratis', 'Programar', 'Linguagens',
            'Estudar', 'Futuro', 'Sonho', 'Realizar')
for p in palavras:
    print(f'\nNa Palavra {p.upper()} Temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')