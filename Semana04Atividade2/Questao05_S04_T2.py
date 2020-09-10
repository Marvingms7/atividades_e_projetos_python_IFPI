def e_crescente(a, b, c, cond=True, condd=True, conddd=True):
    if cond:
        return c, b, a
    elif condd:
        return b, c, a
    elif conddd:
        return a, b, c
    elif a == b > c:
        return c, a, b
    elif a == c > b:
        return b, a, c
    elif b == c > a:
        return a, b, c
    elif c == a < b:
        return a, c, b
    elif a == b < c:
        return a, b, c
    elif b == c < a:
        return b, c, a
    else:
        return f'todos os numeros sao iguais'


def main():
    #Entrada:
    n = int(input("Digite o primeiro numeros: "))
    n2 = int(input("Digite o segundo numero: "))
    n3 = int(input("Digite o terceiro numero: "))
    #Processamento:
    resultado = e_crescente(n, n2, n3, n > n2 and n2 > n3, n > n3 and n3 > n2, n3 > n2 and n2 > n)
    #saida:
    print(f'{resultado}')


if __name__ == '__main__':
    main()
