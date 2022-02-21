expr = str(input('Digite Uma Expressão :'))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua Expressão Esta Valida')
else:
    print('Sua Expressão Esta Errada')
