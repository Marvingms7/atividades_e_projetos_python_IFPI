def carrega_cidades():
    resultado = []
    m = str(int(input()))
    p = int(input())
    res = e_mes(int(m))
    ress = str(res).upper()
    print(f'CIDADES COM MAIS DE {p} HABITANTES E ANIVERSÁRIO EM {ress}:')
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            for n in (1, 5557):
                res = e_mes(int(m))
                if mes == m and int(pop) > p:
                    pplc = pop.split()
                    print(f'{nome}({uf}) tem {pplc[0]} habitantes e faz aniversário em {dia} de {res}.')
                    break
    arquivo.close()
    return resultado

def e_mes(a):
    mess = (
    'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro',
    'dezembro')
    for c in range(len(mess)):
        if a - 1 == c:
            return (mess[c])


cidades = carrega_cidades()