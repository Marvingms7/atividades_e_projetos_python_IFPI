def n_sorte(a):
    a2 = a // 1 % 10
    a3 = a // 10 % 10
    a4 = a // 100 % 10
    a5 = a // 1000 % 10
    a6 = a // 10000 % 10
    a7 = a // 100000 % 10
    a8 = a // 1000000 % 10
    a9 = a // 10000000 % 10
    total = a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9
    return  total


def main():
    n = int(input('Digite sa data de aniversario "ddmmaaaa": '))
    resultado = n_sorte(n)
    print(f'{resultado} é seu numero da sorte!')


if __name__ == '__main__':
    main()