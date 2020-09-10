def a_idade(a3, n3):
    return n3 - a3

def main():
    #Entrada:
    n = int(input("Digite o dia atual: "))
    n2 = int(input("Digite o mês atual: "))
    n3 = int(input("Digite o ano atual: "))
    a = int(input("Digite o dia do seu nascimento: "))
    a2 = int(input("Digite o mês do seu nascimentou: "))
    a3 = int(input("Digite o ano do seu nascimento: "))
    #Processamento:
    idade = a_idade(a3, n3)
    #Saida:
    print(f'A sua idade é:{idade} Anos')

if __name__ == '__main__':
    main()

