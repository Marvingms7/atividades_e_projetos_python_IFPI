nome = []
altura = []
cont = 0
media = 0
maisAlto = 0
maior_q_media = 0
for c in range(1,13):
    n = str(input())
    a = float(input())
    nome.append(n)
    altura.append(a)
maior = altura.index(max(altura))
print(f'JOGADOR MAIS ALTO DO TIME\n{nome[maior]}')
for mai in altura:
    if mai < 0:
        maisAlto = mai
    else:
        if mai > maisAlto:
            maisAlto = mai

print(f'{maisAlto:.2f}')

for med in altura:
    media += med
    cont += 1
mediaTotal = media / cont
print(f'ALTURA MÉDIA DO TIME\n{mediaTotal:.2f}')
print(f'JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')

cont2 = -1
for c in altura:
    cont2 += 1
    if c > mediaTotal:
        print(f'{nome[cont2]}\n{c:.2f}')









