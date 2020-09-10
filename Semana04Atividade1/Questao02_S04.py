def e_menor(a, a2, a3, n, n2, n3):
    if a3 < n3:
         return f' A segunda data é mais recente '
    elif a3 == n3 and a2 < n2:
         return f' A segunda data é mais recente'
    elif a3 == n3 and a2 == n2 and a < n:
         return f' A segunda data é mais recente'
    elif a3 == n3 and a2 == n2 and a == n:
        return f' As duas datas são iguais'
    else:
        return f'A primera data é mais recente'
def main():
    #Entrada:
    a = int(input("Digite o dia da primeira data: "))
    a2 = int(input("Digite o mês da primeira data: "))
    a3 = int(input("Digite o ano da primeira data: "))

    n = int(input("Digite o dia da segunda data: "))
    n2 = int(input("Digite o mês da segunda data: "))
    n3 = int(input("Digite o ano da segunda data: "))
    #Processamento:
    resultado = e_menor(a, a2, a3, n, n2, n3)
    #Saida:
    print(f'A data mais recente é: {resultado}')

if __name__ == '__main__':
    main()