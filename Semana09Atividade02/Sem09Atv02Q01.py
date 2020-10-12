n = int(input())
matriz = []
for l in range(0, n):
    linha = []
    for c in range(0, n):
        num = int(input())
        linha.append(num)
    matriz.append(linha)
maior = matriz[0][0]
menor = matriz[0][0]
maior_linha = 0
maior_coluna = 0
menor_linha = 0
menor_coluna = 0
for l in range(0, n):
    for c in range(0, n):
        if maior < matriz[l][c]:
            maior = matriz[l][c]
            maior_linha = l
            maior_coluna = c
        if menor > matriz[l][c]:
            menor = matriz[l][c]
            menor_linha = l
            menor_coluna = c
print(f'({maior_linha}, {maior_coluna})\n({menor_linha}, {menor_coluna})')