def e_par(n, n1, n2, condicao=True, cond=True):
    if condicao and cond:
        print(f'Os dois digitos sao ímpares')
    elif condicao:
        print(f'Apenas um digito é impar')
    elif cond:
        print(f'Apenas um digito é ímpar')
    else:
        print('Nenhum digito é ímpar.')
def main():
    #Entrada:
    n = int(input("Digite um número entre 10 e 99: "))
    #Processamento:
    n1 = n // 10 % 10
    n2 = n // 1 % 10
    resultado = e_par(n, n1, n2, n1 % 2 == 1, n2 % 2 == 1)
    #Saida:
    f'{resultado}'

if __name__ == '__main__':
    main()


