valores = []
for cont in range(0, 5):
   n = int(input('Digite Um Numero:'))
   if cont == 0 or n > valores[-1]:
      valores.append(n)
      print('Adicionado Ao Final Da Lista')
   else:
      pos = 0
      while pos < len(valores):
          if n <= valores[pos]:
              valores.insert(pos, n)
              print(f'Adicionado Na Posição {pos} Da Lista')
              break
          pos += 1
print('-=-'*20)
print(f'Os Valores Digitados Na Ordem Correta Foram {valores}')