def media(n1, n2, n3):
    n4 = n1 + n2 + n3
    n5 = (n1 + n2 + n3) / 3
    if n5 >= 10:
        return f'10'
    else:
        if n5 != 10 and n5 != 9 and n2 != 9 and n1 != 9 and n3 != 9:
            return n5 + 1
        else:
            if n3 >= 8 and n3 != 9 and n3 != 10:
                n5 + 1
            else:
                if n5 + 1 >= 10:
                    return f'10'



def main():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    resultado = media(n1, n2, n3)
    print (f'{resultado}')


if __name__ == '__main__':
    main()