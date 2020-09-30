def e_valor(a):
    h = 1
    contador = 0
    while True:
        contador += 1
        if contador >= 2:
            h += 1 / contador
            if contador == a:
                return h


def main():
    n = int(input())
    resultado = e_valor(n)
    print(f'{resultado:.4f}')


if __name__ == '__main__':
    main()