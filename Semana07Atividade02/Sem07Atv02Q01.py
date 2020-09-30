n = int(input("Digite um numero: "))
contador = 0
acumulador = 0
total = n
while True:
    if n == 0:
        acumulador = 1
        break
    contador += 1
    if n == contador: break
    acumulador = total * contador
    total = acumulador


print(f'{acumulador}')
