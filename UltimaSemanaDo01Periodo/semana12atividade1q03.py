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


def lista_vereadores(arquivos, cadeiras):
    lista = []
    ordenado = sorted(arquivos, key=itemgetter('Votos'), reverse=True)
    cont = 0
    for o in ordenado:
        cont += 1
        if cont <= int(cadeiras):
            lista.append(o)
    ordem = sorted(lista, key=itemgetter('Votos'), reverse=True)
    print('CANDIDATOS MAIS VOTADOS PARA QUANTIDADE DE CADEIRAS')
    print('Número', '' * 1, 'Nome do Candidato', ' ' * 16, 'Votos * Partido (coligação)')
    for o in ordem:
        print(f"{o['Número']:<7} {o['Nome do Candidato']:<35} {o['Votos']:4} * {o['Partido']} ({o['coligação']})")


def main():
    nome = input().strip()
    CADEIRAS = input()
    candidatos = carregar_candidatos(nome)
    lista_vereadores(candidatos, CADEIRAS)

if __name__ == '__main__':
    main()
