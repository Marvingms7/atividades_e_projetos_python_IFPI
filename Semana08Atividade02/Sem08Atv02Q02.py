numeros = []
def repetido(a):
    numeros.append(a)
    contador = 0
    while True:
        a = int(input())
        if a == 0:break
        numeros.append(a)
    m = int(input())
    total = numeros.count(m)
    return (f'{m}\n{total}')


def main():
    n = int(input())
    resultado = repetido(n)
    print(f'{numeros}\n{resultado}')

if __name__ == '__main__':
    main()


