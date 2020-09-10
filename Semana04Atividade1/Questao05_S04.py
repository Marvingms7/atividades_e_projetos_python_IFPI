def o_imc(n, n2):
    m = n2 * n2
    p = n / m
    if p <= 18.5:
        return f'A baixo do peso'
    elif p <= 25:
        return  f'Peso normal'
    elif p <= 30:
        return f'Sobrepeso'
    elif p <= 35:
        return f'Obeso leve'
    elif p <= 40:
        return f'Obeso moderado'
    elif p >= 40:
        return  f'Obeso mórbido'

def main():
    #Entrada:
    n = float(input("Digite seu peso: "))
    n2 = float(input("Digite sua altura: "))
    #Processamento
    resultado = o_imc(n, n2)
    #Saida:
    print(f'{resultado}')

if __name__ == '__main__':
    main()