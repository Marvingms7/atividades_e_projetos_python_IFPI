meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
filiais = ('Filial 1', 'Filial 2', 'Filial 3')
ano = ('2014', '2015', '2016', '2017')
ano2014 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
ano2015 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
ano2016 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
ano2017 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
total14 = []
totall14 = []

for l in range(0, 12):
    for c in range(0, 3):
        ano2014[l][c] = int(input("Digite um numero: "))
print(f'-=' * 12)
for l in range(0, 12):
    for c in range(0, 3):
        print(f'[{ano2014[l][c]:^5}]', end='')
    print()
print(f'-=' * 12)
for l in range(0, 12):
    for c in range(0, 3):
        ano2015[l][c] = int(input("Digite um numero: "))
print(f'-=' * 12)
for l in range(0, 12):
    for c in range(0, 3):
        print(f'[{ano2015[l][c]:^5}]', end='')
    print()
print(f'-=' * 12)
for l in range(0, 12):
    for c in range(0, 3):
        ano2016[l][c] = int(input("Digite um numero: "))
print(f'-=' * 12)
for l in range(0, 12):
    for c in range(0, 3):
        print(f'[{ano2016[l][c]:^5}]', end='')
    print()
print(f'-=' * 12)
for l in range(0, 12):
    for c in range(0, 3):
        ano2017[l][c] = int(input("Digite um numero: "))
print(f'-=' * 12)
for l in range(0, 12):
    for c in range(0, 3):
        print(f'[{ano2017[l][c]:^5}]', end='')
    print()
print(f'-=' * 12)
def e_soma(a):
    soma1 = soma2 = soma3 = 0
    for l in range(0, 12):
        for c in range(0, 3):
            if c == 0:
                soma1 += a[l][0]
    for l in range(0, 12):
        for c in range(0, 3):
            if c == 1:
                soma2 += a[l][1]
    for l in range(0, 12):
        for c in range(0, 3):
            if c == 2:
                soma3 += a[l][2]

    return f'{filiais[0]};{soma1:.1f}, {filiais[1]};{soma2:.1f}, {filiais[2]};{soma3:.1f}'

def e_soma_total_por_ano(a):
    somaTotal_por_ano = 0
    for l in range(0, 12):
        for c in range(0, 3):
            somaTotal_por_ano += a[l][c]
    return f'{somaTotal_por_ano}'
def e_periodo(a):
    soma1 = soma2 = soma3 = soma4 = soma5 = soma6 = soma7 = soma8 = soma9 = soma10 = soma11 = soma12 = 0
    for l in range(0, 12):
        for c in range(0, 3):
            if l == 0:
                soma1 += a[l][c]
            if l == 1:
                soma2 += a[l][c]
            if l == 2:
                soma3 += a[l][c]
            if l == 3:
                soma4 += a[l][c]
            if l == 4:
                soma5 += a[l][c]
            if l == 5:
                soma6 += a[l][c]
            if l == 6:
                soma7 += a[l][c]
            if l == 7:
                soma8 += a[l][c]
            if l == 8:
                soma9 += a[l][c]
            if l == 9:
                soma10 += a[l][c]
            if l == 10:
                soma11 += a[l][c]
            if l == 11:
                soma12 += a[l][c]

    return f'{meses[0]};{soma1}\n{meses[1]};{soma2}\n{meses[2]};{soma3}\n{meses[3]};{soma4}\n{meses[4]}:{soma5}\n{meses[5]};{soma6}\n{meses[6]};{soma7}\n{meses[7]};{soma8}\n{meses[8]};{soma9}\n{meses[9]};{soma10}\n{meses[10]};{soma11}\n{meses[11]};{soma12}'


som1 = e_soma(ano2014)
som2 = e_soma(ano2015)
som3 = e_soma(ano2016)
som4 = e_soma(ano2017)
tot1 = e_soma_total_por_ano(ano2014)
tot2 = e_soma_total_por_ano(ano2015)
tot3 = e_soma_total_por_ano(ano2016)
tot4 = e_soma_total_por_ano(ano2017)
pe1 = e_periodo(ano2014)
pe2 = e_periodo(ano2015)
pe3 = e_periodo(ano2016)
pe4 = e_periodo(ano2017)
print(f'Total de cada ano por filial:')
print(f'2014;{som1}\n2015;{som2}\n2016;{som3}\n2017;{som4}\n', end='')
print(f'Total de todas as filiais por ano:')
print(f'Total 2014 todas filiais;{tot1}\nTotal 2015 todas filiais;{tot2}\nTotal 2016 todas filiais;{tot3}\nTotal 2017 todas filiais;{tot4}\n', end='')
print(f'A soma por periodo no ano de 2014 é de:\n{pe1}')
print(f'A soma por periodo no ano de 2015 é de:\n{pe2}')
print(f'A soma por periodo no ano de 2016 é de:\n{pe3}')
print(f'A soma por periodo no ano de 2017 é de:\n{pe4}')










