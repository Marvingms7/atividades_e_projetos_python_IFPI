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
                    "Nome do Candidato": str(nomes),
                    "Votos": int(votos),
                    "Partido": str(partido),
                    "coligação": str(coligacao),
                }
            )

    return dados


def dados_candidatos(arquivo):
    ordenado = sorted(arquivo, key=itemgetter('Votos'), reverse=True)

    return ordenado


def main():
    nome = input().strip()
    candidatos = carregar_candidatos(nome)
    ordenado = dados_candidatos(candidatos)

    print('DADOS DOS CANDIDATOS')
    print(
        f"{'Número':<8s}"
        f"{'Nome do Candidato':30s}"
        f"{'Votos':>10s} * "
        f"{'Partido (coligação)':50s}"
    )
    for d in ordenado:
        print(
            f"{d['Número']:<8d}"
            f"{d['Nome do Candidato']:30s}"
            f"{d['Votos']:>10d} * "
            f"{d['Partido'] + ' (' + d['coligação'] + ')':50s}"
        )


if __name__ == '__main__':
    main()
