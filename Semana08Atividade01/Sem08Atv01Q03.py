list = []
n = int(input())
contador = 0
for c in range(1, n + 1):
    num = float(input())
    list.insert(contador, num)
    contador -= n
print(f'{list}')

notas = []
contador2 = 0
media = 0
m = 0
for b in range(1, n + 1):
    num = float(input())
    contador2 += 1
    media += num
    notas.append(num)
    m = media / n

if contador2 == 0:
    print(f'{notas}\nSEM NOTAS')
else:
    print(f'{notas}\n{m:.1f}')

contador3 = 0
consoante = []
for a in range(1, n + 1):
    letra = str(input())[0]
    letra == letra.upper()
    if letra in 'AaEeIiOoUu':
        contador3 += 1
    elif letra in 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTVvWwXxYyZz':
        consoante.append(letra)


print(f'{contador3}\n{consoante}')



