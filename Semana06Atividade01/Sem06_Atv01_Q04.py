inv = 0
n = int(input("Digite um numero: "))
while n > 0:
    inv = (inv * 10) + n % 10
    n //= 10

print(f'{inv}')


