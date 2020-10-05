nome = []
idade = []
altura = []
acumulador = 0
contador = 0
media = 0
mediaTotal = 0
cont2 = -1
for c in range(1,31):
    nome.append(str(input()))
    idade.append(int(input()))
    altura.append(float(input()))

for c in altura:
    contador += 1
    media += c
mediaTotal = round(media / contador, 2)
print(f'MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')

for id in idade:
    cont2 += 1
    if id > 13 and altura[cont2] < mediaTotal:
        print(f'{nome[cont2]}')














