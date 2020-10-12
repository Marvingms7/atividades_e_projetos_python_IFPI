def carrega_cidades():
    resultado = []
    n = int(input())
    print(f'CIDADES COM MAIS DE {n} HABITANTES:')
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            for c in (1, 5558):
                pop = int(pop)
                if pop >= n:
                    print(f'IBGE: {ibge} - {nome}({uf}) - POPULAÇÃO: {pop}')
                    break

    arquivo.close()
    return resultado


cidades = carrega_cidades()

