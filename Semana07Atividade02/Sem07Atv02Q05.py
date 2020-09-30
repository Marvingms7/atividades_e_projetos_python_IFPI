n = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

def primo(a):
    contador = 0
    for c in range(1, n + 1):
        if n % c == 0:
            contador += 1

    if contador == 2:
        print(f'{c}')

for n in range(n, n2+1):
    if primo(n):
        print(n)

