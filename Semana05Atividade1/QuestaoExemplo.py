def e_par(n):
    return n % 2 == 0

def numeros_pares(inicio, quantidade):
    if e_par(inicio):
        proximo = inicio + 2
    else:
        proximo = inicio + 1

    numeros_pares = ' '    
    for n in range(quantidade):
        numeros_pares += str(proximo) + ' '
        proximo += 2
    return numeros_pares.strip()
    

def main():
    num_inicio = int(input("inicio do intervalo: "))
    qtd = int(input("Quantidade de numeros pares: "))
    print(f'{qtd} pares apos {num_inicio}')
    print(numeros_pares(num_inicio, qtd)) 


if __name__ == '__main__':
    main()
          