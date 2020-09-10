def max_min():
    print(max(n, n2, n3, n4, n5))
    print(min(n, n2, n3, n4, n5))
    media = (n + n2 + n3+ n4 + n5) / 5
    print(f'{media}')


def main():
    max_min()

n = float(input("Digite um numero: "))
n2 = float(input("Digite um numero: "))
n3 = float(input("Digite um numero: "))
n4 = float(input("Digite um numero: "))
n5 = float(input("Digite um numero: "))

if __name__ == '__main__':
    main()