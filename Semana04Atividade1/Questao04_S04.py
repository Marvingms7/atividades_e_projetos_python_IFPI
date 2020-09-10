def a_media(a, b, c, d, e,cond=True):
    media = (a + b + c + d + e) / 5
    if a > media and b > media and c > media:
        return a, b, c
    elif a > media and b > media and d > media:
        return a, b, d
    elif a > media and b > media and e > media:
        return  a, b, e
    elif a > media and c > media and d > media:
        return a, c, d
    elif a > media and c > media and e > media:
        return a, c, e
    elif a > media and d > media and e > media:
        return  a, d, e
    else:
        return f'Os numeros são abaixo da media ou iguais a ela'





def main():
    #Entrada:
    n = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a segunda nota: "))
    n3 = int(input("Digite a terceira nota: "))
    n4 = int(input("Digite a quarta nota: "))
    n5 = int(input("Digite a quinta nota: "))
    #Processamento:
    media = (n + n2 + n3 + n4 + n5) / 5
    resultado = a_media(n, n2, n3, n4, n5, n > n2 or n > n3)
    #Saida:
    print(f'{resultado}')
    print(f'{media}')

if __name__ == '__main__':
    main()