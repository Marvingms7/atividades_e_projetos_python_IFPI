
n = int(input())
contador =0
for c in range(1, n + 1):
    if n % c == 0:
        contador += 1

if contador == 2:
    print(f'True')
else:
    print(f'False')