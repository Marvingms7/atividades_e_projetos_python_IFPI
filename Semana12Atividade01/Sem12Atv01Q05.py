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


def media_preco(a):
        mes = int(input("Digite o mes em que deseja saber a média: "))
        ano = int(input("Digite o ano em que deseja saber a média: "))
        print(f'Dias de {mes}/{ano} que houve queda no preço da ação:')
        ordenado = sorted(a, key=itemgetter('ano', 'mes', 'dia'))
        for p in ordenado:
            if p['mes'] == mes:
                if p['ano'] == ano:
                    if p['abertura'] > p['fechamento']:
                        d = p['dia']
                        v = round(p['abertura'] - p['fechamento'], 3)
                        print(f"('{p['dia']:02d}/{p['mes']:02d}/{p['ano']}', {p['abertura']}, {p['fechamento']}, {v})")

def main():
    # Carregar os dados da empresa a partir do arquivo csv
    a_carregar = input("Digite o nome do arquivo.csv em que deseja abrir: ").strip()
    abev3 = carregar(a_carregar)
    # Mostra em quais dias de um mês e ano houve queda no preço da ação, Preço de abertura, preço do fechamento na data e a variação da moeda corrente
    media_preco(abev3)



if __name__ == '__main__':
    main()