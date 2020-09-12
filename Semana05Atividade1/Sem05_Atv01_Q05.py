def maior():
    n_maior = 0

    for k in range(0, 100):
        a = int(input("Digite um numero: "))
        if a > n_maior:
            n_maior = a
    return n_maior


def main():
    res = maior()
    print(f'O maior numero é {res}')

if __name__ == '__main__':
    main()


