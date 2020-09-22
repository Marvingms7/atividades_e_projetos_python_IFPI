maior = 0
menor = 0
contador = 0
while True:
    n = int(input("Digite um numero: "))
    contador += 1
    if n == 0: break
    if contador == 1:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f'maior é {maior}, e o menor é {menor}')







