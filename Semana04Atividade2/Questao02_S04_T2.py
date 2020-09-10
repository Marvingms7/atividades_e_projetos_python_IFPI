def par(n,n1, n2, n3,condicao=False, cond=False, con=False):
    if condicao and cond and con:
        print(f' todos os numero sao pares')
    elif condicao and cond:
        print(f' Apenas 2 numeros sao par')
    elif condicao and con:
        print(f' apenas 2 numeros sao par')
    elif cond and con:
        print(f' Apenas 2 numeros sao par')
    elif condicao:
        print(f'Apenas 1 numero é par')
    elif cond:
        print(f'Apenas 1 numero é par')
    elif con:
        print(f' Apenas 1 numero é par')
    else:
        print(f'todos os numero sao ímpares')


def main():
    #entrada:
    n = int(input('Digite um número entre 100 e 999: '))
    #Processamento:
    n1 = n // 100 % 10
    n2 = n // 10 % 10
    n3 = n// 1 % 10
    resultado = par(n,n1, n2, n3, n1 % 2 != 1, n2 % 2 !=1, n3 % 2 !=1)
    #Saida:
    f'{resultado}'


if __name__=='__main__':
    main()