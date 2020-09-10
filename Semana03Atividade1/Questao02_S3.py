def e_impar(n1):
    return n1 % 2 != 0


def main():
    n1 = int(input("Digite um numero: "))
    resultado = e_impar(n1)
    print(f' o numero impar é:{resultado}')

if __name__ == '__main__':
    main()