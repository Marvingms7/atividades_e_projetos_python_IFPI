def e_temp(a):
    if a[1] == 'C' and  a[3] == 'C' and a[0] > a[2]:
        maior = a[0]
        esc = 'C'
    elif a[1] == 'C' and a[3] == 'C' and a[0] < a[2]:
        maior = a[2]
        esc = 'C'
    elif a[1] == 'F' and a[3] == 'F' and a[0] > a[2]:
        maior = a[0]
        esc = 'F'
    elif a[1] == 'F' and a[3] == 'F' and a[0] < a[2]:
        maior = a[2]
        esc = 'F'
    elif a[1] == 'C' and a[3] == 'F':
        F = (a[0] * (9/5)) + 32
        if a[0] > F:
            maior = F
            esc = 'C'
        else:
            maior = a[2]
            esc = 'F'

    elif a[1] == 'F' and a[3] == 'C':
        C = (a[0] - 32) * (5/9)
        if a[0] > C:
            maior = C
            esc = 'F'
        else:
            maior = a[2]
            esc = 'C'

    m = []
    m.append(maior)
    m.append(esc)
    mm = tuple(m)

    return (f'{mm}')

def e_soma(a):
    if a[1] == 'C' and a[3] == 'C':
        som = a[0] + a[2]
        esc = 'C'
    elif a[1] == 'F' and a[3] == 'F':
        som = a[0] + a[2]
        esc = 'F'
    elif a[1] == 'F' and a[3] == 'C':
        C = (a[0] - 32) * (5/9)
        som = C + a[2]
        esc = 'C'
    elif a[1] == 'C' and a[3] == 'F':
        F = (a[0] * (9/5)) + 32
        som = F + a[2]
        esc = 'F'
    som = round(som, 4)
    tot = []
    tot.append(som)
    tot.append(esc)
    total = tuple(tot)
    return (f'{total}')






def main():
    temperatura = (float(input()),
                str(input()).upper()[0],
                float(input()),
                str(input()).upper()[0])
    temperaturaa = e_temp(temperatura)
    resultado = e_soma(temperatura)
    print(f'{resultado}')

if __name__ == '__main__':
    main()