matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaL = somaC = contador = media = maior = menor = 0
for l in range(0, 4):
    for c in range(0, 3):
        matriz[l][c] = int(input("Digite um valor: "))
print(f'-=' * 12)
for l in range(0, 4):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'-=' * 12)
for l in range(0, 3):
    somaL += matriz[0][l]
for c in range(0, 4):
    somaC += matriz[c][2]
for l in range(0, 4):
    for c in range(0, 3):
        media += matriz[l][c]
        contador += 1
media = media / contador
for l in range(0, 4):
    for c in range(0, 3):
        if l == 0 and c == 0:
            maior = menor = matriz[l][c]
        if matriz[l][c] > maior:
            maior = matriz[l][c]
        if matriz[l][c] < menor:
            menor = matriz[l][c]



print(f'a soma dos elementos da primeira linha é:{somaL}\na soma dos elementos da ultima coluna é:{somaC}\na média dos elementos é:{media:.2f}\no menor elemento é:{menor}\no maior elemento é:{maior}')




