from operator import itemgetter


def carregar_candidatos(arquivo):
    dados = []
    with open(arquivo) as f:
        for linha in f.readlines():
            nomes, numeros, partido, coligacao, votos = linha.strip().split(';')
            if "'" in coligacao:
                coligacao = coligacao - "'"
            dados.append(
                {
                    "Número": int(numeros),
                    "Nome do Candidato": nomes,
                    "Votos": int(votos),
                    "Partido": partido,
                    "coligação": coligacao,
                }
            )

    return dados


def carregar_coligacoes(arquivos, cadeiras):
    total_cadeiras = c = maior = 0
    coligacao = []
    ordenado = sorted(arquivos, key=itemgetter('coligação'), reverse=True)
    for linha in ordenado:
        if linha['coligação'] not in coligacao:
            coligacao.append(linha['coligação'])
    votos_validos = 0
    for c in range(0, len(coligacao)):
        soma = 0
        for d in ordenado:
            if coligacao[c] == d['coligação']:
                soma += d['Votos']
        votos_validos += soma

    dados_da_coligacao = []
    for i in coligacao:
        soma = QE = 0
        for d in ordenado:
            if i == d['coligação']:
                soma += d['Votos']
        QE = round(votos_validos / int(cadeiras))

        if soma < QE:
            QP = 0
        else:
            QP = round(soma / QE)

        dados_da_coligacao.append(
            {
                "Coligação": i,
                "Total de Votos": int(soma),
                "Total de Vagas": int(QP),
            }
        )

    ordem = sorted(dados_da_coligacao, key=itemgetter('Total de Vagas', 'Total de Votos'), reverse=True)
    print('DADOS DAS COLIGAÇÕES')
    print('Coligação                                               Total de Votos      Total de Vagas')
    for i in ordem:
        print(f"{i['Coligação']:<55} {i['Total de Votos']:>14} {i['Total de Vagas']:>19}")


def main():
    nome = input().strip()
    CADEIRAS = input()
    candidatos = carregar_candidatos(nome)
    carregar_coligacoes(candidatos, CADEIRAS)


if __name__ == '__main__':
    main()

