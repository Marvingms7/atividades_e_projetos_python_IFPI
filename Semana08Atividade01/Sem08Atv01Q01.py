valores = []
soma = 0
mult = 1
for c in range(0, 10):
    a = int(input())
    valores.append(a)
    soma += a
    mult *= a
print(f'{valores}\n{soma}\n{mult}')