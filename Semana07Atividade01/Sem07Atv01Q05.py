n = int(input("Escreva quantidade de aves no inicio do ano 1600: "))
mortos = (6 / 100) * n
nascidos = (1 / 100) * n
total_populacao = (n - mortos) + nascidos
populacao_in= (10 / 100) * n
ano = 1600
print(f'{ano},{nascidos:.0f},{mortos:.0f},{total_populacao:.0f}')
while True:
    ano += 1
    if total_populacao > populacao_in:
        nascidos = (1 / 100) * total_populacao
        mortos = (6 / 100) * total_populacao
        total_populacao = (total_populacao - mortos) + nascidos
    else:
        break

    print(f'{ano},{nascidos:.0f},{mortos:.0f},{total_populacao:.0f}')