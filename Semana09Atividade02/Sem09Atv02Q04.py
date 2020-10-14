vendas = [ [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
maior = marca = media = contador = maior1 = maior2 = maior3 = maior4 = maior5 = maior6 = maiorN = anoo = 0
for l in range(0, 4):
    for c in range(0, 6):
        vendas[l][c] = int(input("Digite os dados para a tabela: "))
for l in range(0, 4):
    for c in range(0, 6):
        print(f'[{vendas[l][c]:^5}]', end='')
    print()
ano = str(input("Digite um ano: "))
if ano == '2013':
    for l in range(0, 4):
        for c in range(0, 6):
            if l == 0 and c == 0:
                maior = vendas[l][0]
                marca = l + 1
            if vendas[l][0] > maior:
                maior = vendas[l][0]
                marca = l + 1

elif ano == '2014':
    for l in range(0, 4):
        for c in range(0, 6):
            if l == 0 and c == 0:
                maior = vendas[l][1]
                marca = l + 1
            if vendas[l][1] > maior:
                maior = vendas[l][1]
                marca = l + 1
elif ano == '2015':
    for l in range(0, 4):
        for c in range(0, 6):
            if l == 0 and c == 0:
                maior = vendas[l][2]
                marca = l + 1
            if vendas[l][2] > maior:
                maior = vendas[l][2]
                marca = l + 1
elif ano == '2016':
    for l in range(0, 4):
        for c in range(0, 6):
            if l == 0 and c == 0:
                maior = vendas[l][3]
                marca = l + 1
            if vendas[l][3] > maior:
                maior = vendas[l][3]
                marca = l + 1
elif ano == '2017':
    for l in range(0, 4):
        for c in range(0, 6):
            if l == 0 and c == 0:
                maior = vendas[l][4]
                marca = l + 1
            if vendas[l][4] > maior:
                maior = vendas[l][4]
                marca = l + 1
elif ano == '2018':
    for l in range(0, 4):
        for c in range(0, 6):
            if l == 0 and c == 0:
                maior = vendas[l][5]
                marca = l + 1
            if vendas[l][5] > maior:
                maior = vendas[l][5]
                marca = l + 1
if marca == 1:
    marca = 'Fiat'
elif marca == 2:
    marca = 'Ford'
elif marca == 3:
    marca = 'GM'
elif marca == 4:
    marca = 'Wolkswagen'

for l in range(0, 4):
    for c in range(0, 6):
        media += vendas[l][c]
        contador += 1
media = media / contador

for l in range(0, 4):
    for c in range(0, 6):
        if c == 0:
            maior1 += vendas[l][0]
for l in range(0, 4):
    for c in range(0, 6):
        if c == 1:
            maior2 += vendas[l][1]
for l in range(0, 4):
    for c in range(0, 6):
        if c == 3:
            maior3 += vendas[l][2]
for l in range(0, 4):
    for c in range(0, 6):
        if c == 3:
            maior4 += vendas[l][3]
for l in range(0, 4):
    for c in range(0, 6):
        if c == 4:
            maior5 += vendas[l][4]
for l in range(0, 4):
    for c in range(0, 6):
        if c == 5:
            maior6 += vendas[l][5]

maiorN = max(maior1, maior2, maior3, maior4, maior5, maior6)
if maiorN == maior1:
    anoo = '2013'
elif maiorN == maior2:
    anoo = '2014'
elif maiorN == maior3:
    anoo = '2015'
elif maiorN == maior4:
    anoo = '2016'
elif maiorN == maior5:
    anoo = '2017'
elif maiorN == maior6:
    anoo = '2018'


print(f'O fabricante que mais vendeu no ano de {ano} foi {marca} e a maior venda foi de {maior} veiculos\nJuntas todas as marcas tiveram uma media de vendas de {media:.2f} durante o periodo de 2013 a 2018\nO ano de maior volume de vendas foi {anoo}, com a media de {maiorN} em vendas')






