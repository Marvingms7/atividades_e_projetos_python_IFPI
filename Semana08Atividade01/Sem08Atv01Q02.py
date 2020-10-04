numtupla = []
numtuplab = numtupla[:]
n = int(input("Digite um numero: "))
for c in range(1, n + 1):
    numtupla.append(c)
    numtuplab.insert(c, 0)
print(f'{numtuplab}\n{numtupla}')

ordenado = []
for b in range(1, n + 1):
    numAleatorio = int(input(f'Digite {n} numeros aleatorios: '))
    ordenado.append(numAleatorio)
print(f'{ordenado}')

invertido = []
contador = 0
for d in range(1, n + 1):
    numInvertido = int(input(f'Digite {n} numeros aleatorios: '))
    invertido.insert(contador, numInvertido)
    contador -= n

print(f'{invertido}')


