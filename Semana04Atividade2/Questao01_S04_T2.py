def e_total(n, n2):
    m = len(n)
    if n2 == 1:
        n3 = str(input("Qual o nome do seu parceiro(a): "))
        m2 = len(n3)
        return m + m2
    elif n2 == 2:
        return m


def main():
    #Entrada:
    n = str(input("Digite seu nome: "))
    n2 = int(input('Digite "1" se for casado(a) e "2" se for solteiro(a): '))

    #Processamento:
    resultado = e_total(n, n2)
    #Saida:
    print(f'{resultado}')

if __name__ == '__main__':
    main()
