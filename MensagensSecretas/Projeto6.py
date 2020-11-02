casal = input("Digite o nome de duas pessoas para ver a porcentagem de compatibilidade ex:(Romeu e julieta): ").lower().strip()
pontos = 0
for i in casal:
    if i in 'aeiou':
        pontos += 10
    elif i in 'amor':
        pontos += 10
if pontos <= 10:
    print(f'Placar de compatibilidade abaixo que 10%, total de {pontos} pontos\nEsqueça essa pessoa, vocês nunca vão da certo! :(')
elif pontos >= 10  and pontos <= 20:
    print(f'Placar de compatibilidade entre 10% e 20%, total de {pontos} pontos\nInfelismente é bem dificil vocês darem certo! :(')
elif pontos >= 30 and pontos <= 50:
    print(f'Placar de compatibilidade entre 30% e 50%, total de {pontos} pontos\nSe âmbos se esforçarem podem da certo! :) :)')
elif pontos >= 50 and pontos <= 70:
    print(f'Placar de compatibilidade entre 50% e 70%, total de {pontos} pontos\nA chance de vocês formarem um casal é boa! S2 S2')
elif pontos >= 80 and pontos <= 100:
    print(f'Placar de compatibilidade entre 80% e 100%, total de {pontos} pontos\nVocês formam um casal perfeito!! :) :) S2 S2 S2')


