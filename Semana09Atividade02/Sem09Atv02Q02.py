mes = []
e = []
C = []
soma = 0
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro',
    'Dezembro')
for m in range(len(meses)):
    t = float(input())
    esc = input().upper()[0]
    if esc == 'C':
        T = round(t + 273.15, 2)
    if esc == 'F':
        T = round(((t-32)/1.800) + 273.15, 2)
    if esc == 'K':
        T = t
    mes.append(m)
    e.append(T)
    soma = round(soma + T, 2)
media = round(soma/12, 2)
print(f'TEMPERATURA MÉDIA ANUAL\n{media}K')
print('TEMPERATURAS ACIMA DA MÉDIA ANUAL:')
for b,p in zip(mes, e):
    C.append(b)
    C.append(p)
    for n in range(len(meses)):
        if p > media:
            print(f'{meses[b]}: {p}K')
            break