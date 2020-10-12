def carrega_cidades(a,b):
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            for num in (1, 5558):
                if int(dia) == a and int(mes) == b:
                    print(f'{nome}({uf})')
                    break

    arquivo.close()
    return resultado
def e_mes(mess):
    if mess == 1:
        mess = 'JANEIRO'
    elif mess == 2:
         mess = 'FEVEREIRO'
    elif mess == 3:
         mess = 'MARÇO'
    elif mess == 4:
        mess = 'ABRIL'
    elif mess == 5:
        mess = 'MAIO'
    elif mess == 6:
        mess = 'JUNHO'
    elif mess == 7:
        mess = 'JULIO'
    elif mess == 8:
        mess = 'AGOSTO'
    elif mess == 9:
        mess = 'SETEMBRO'
    elif mess == 10:
        mess = 'OUTUBRO'
    elif mess == 11:
        mess = 'NOVEMBRO'
    elif mess == 12:
        mess = 'DEZEMBRO'
    return mess


def main():
    d = int(input())
    m = int(input())
    res = e_mes(int(m))
    print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {d} DE {res}:')
    cidades = carrega_cidades(d,m)




if __name__ == '__main__':
    main()

