listA = []
def comprimento(a):
    cont = 1
    listA.append(a)
    while True:
        n = int(input("Digite um numero para adicionar a uma lista: "))
        if n == 0: break
        listA.append(n)
        cont += 1
    return (f'{cont}')

def inverter(b):
    listaB = listA
    listaB = listA[::-1]
    return (f'{listaB}')

def minimo(a):
    menor = 0
    for c in range(0, len(listA)):
        if c == 0:
            menor = listA[c]
        if listA[c] < menor:
            menor = listA[c]
    return (f'{menor}')

def maximo(a):
    maior = 0
    for c in range(0, len(listA)):
        if c == 0:
            maior = listA[c]
        if listA[c] > maior:
            maior = listA[c]
    return (f'{maior}')

def soma(a):
    s = 0
    for c in listA:
        s += c
    return f'{s}'


def main():
    n = int(input(f'Digite varios numeros e use "0" para finalizar sua lista: '))
    c = comprimento(n)
    i = inverter(n)
    mi = minimo(n)
    ma = maximo(n)
    so = soma(n)
    print(f'{listA}\n{c}\n{i}\n{mi}\n{ma}\n{so}')



if __name__ == '__main__':
    main()











