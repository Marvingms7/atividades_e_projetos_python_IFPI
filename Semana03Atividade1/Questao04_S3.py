def total(n):
    return n <= 9 and n >= 0



def main():
    n = int(input("Digite um numero entre 0 e 9, caso contrario será falso: "))
    resultado = total(n)
    print(f' o numero é {resultado}')

if __name__ == '__main__':
    main()