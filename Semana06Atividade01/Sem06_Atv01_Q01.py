def taixa(n, t, d):
    quantidade = 0
    while n < d:
        m = (n * t) / 100
        n = m + n
        quantidade += 1
    return quantidade


def main():
    n = int(input("Digite o total depositado: "))
    t = int(input("Digite a taxa :"))
    d = n * 2
    qnt = taixa(n, t, d)
    print(f'{qnt}')


if __name__ == '__main__':
    main()
