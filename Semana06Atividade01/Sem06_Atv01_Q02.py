
m = contador = total = 0
while True:
    n = int(input("Digite um numero: "))
    contador += 1
    if n == 0: break
    total += n
    m = total / contador
print(f'{m}')



