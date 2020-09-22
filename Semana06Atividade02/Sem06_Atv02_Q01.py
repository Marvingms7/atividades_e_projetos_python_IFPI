contador = 0
soma = 0
while True:
    contador += 1
    n = int(input("Digite um numero inteiro: "))
    if n == 0: break
    soma += n
print(f'{soma}')