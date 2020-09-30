n = int(input())
contador = 3
c2 = 0
c3 = 1
print(f'{c2}, {c3}', end='')
while n >= contador:
    c4 = c2 + c3
    print(f',', end=' ')
    print(f'{c4}', end='')
    c2 = c3
    c3 = c4
    contador += 1





















