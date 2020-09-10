def e_maior(a, a2, a3, a4, a5):
    if a > a2 and a > a3 and a > a4 and a > a5:
        return f'O Primeiro numero é o maior'
    elif a2 > a and a2 > a3 and a2 > a4 and a2 > a5:
        return f'O Segundo numero  é o maior'
    elif a3 > a and a3 > a2 and a3 > a4 and a3 > a5:
        return f'O Terceiro numero é o maior'
    elif a4 > a and a4 > a2 and a4 > a3 and a4 > a5:
        return f'O Quarto numero é o maior'
    else:
        return f'O Quinto numero é o maior'

def main():
    #Entrada:
    a = int(input("Digite o primeiro numero: "))
    a2 = int(input("Digite o segundo numero: "))
    a3 = int(input("Digite o terceiro numero: "))
    a4 = int(input("Digite o quarto numero: "))
    a5 = int(input("Digite o quinto numero: "))
    #Processamente:
    resultado = e_maior(a, a2, a3, a4, a5)
    #Saida:
    print(f'{resultado}')

if __name__ == '__main__':
    main()
