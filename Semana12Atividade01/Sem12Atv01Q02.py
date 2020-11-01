from operator import itemgetter

def carregar(arquivo):
    linhas = []
    with open(arquivo) as f:
        f.readline()
        for linha in f.readlines():
            data, abertura, alta, baixa, fechamento, volume = linha.strip().split(',')
            ano, mes, dia = data.split('-')
            linhas.append(
                {
                    "ano": int(ano),
                    "mes": int(mes),
                    "dia": int(dia),
                    "abertura": float(abertura),
                    "alta": float(alta),
                    "baixa": float(baixa),
                    "fechamento": float(fechamento),
                    "volume": int(volume),
                }
            )
    return linhas


def formatar_data(linha):
    meses = (
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    )
    d, m, a, = linha['dia'], linha['mes'], linha['ano']
    return f'{d:0>2d} de {meses[m - 1]} de {a}'


def menor_fechamento(a):
    ordenado2 = sorted(a, key=itemgetter('fechamento'))
    return ordenado2[0]['fechamento'], formatar_data(ordenado2[0])


def main():
    # Carregar os dados da empresa a partir do arquivo csv
    a_carregar = input("Digite o nome do arquivo.csv que deseja abrir: ")
    abev3 = carregar(a_carregar)
    # Mostra o menor preço no fechamento
    fechamento, data2 = menor_fechamento(abev3)
    print(f'O menor preço no fechamento foi {fechamento:.2f} em {data2}')




if __name__ == '__main__':
    main()