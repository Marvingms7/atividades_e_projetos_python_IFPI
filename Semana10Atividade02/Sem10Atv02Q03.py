lista = {}
lista2 = []
lista3 = []
lista4 = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}
c1 = c2 = c3 = c4 = c5 = c6 = 0
contador = 0
while True:
    listaa = int(input())
    if listaa != 0 and listaa >= 1 and listaa <= 6:
        lista[listaa] = listaa
        lista2.append(listaa)
        contador += 1
    if listaa == 0:
        break
for c in lista2:
    if c == 1:
        c1 += 1
    if c == 2:
        c2 += 1
    if c == 3:
        c3 += 1
    if c == 4:
        c4 += 1
    if c == 5:
        c5 += 1
    if c == 6:
        c6 += 1
    lista3.append(c1)
    lista3.append(c2)
    lista3.append(c3)
    lista3.append(c4)
    lista3.append(c5)
    lista3.append(c6)

for i in lista.keys():
    if lista[i] == 1:
        lista4[i] = c1
    if lista[i] == 2:
        lista4[i] = c2
    if lista[i] == 3:
        lista4[i] = c3
    if lista[i] == 4:
        lista4[i] = c4
    if lista[i] == 5:
        lista4[i] = c5
    if lista[i] == 6:
        lista4[i] = c6
print(f"o dado foi jogado {contador} vezes")
lista5 = lista4.keys()
for i in lista4:
    if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6:
        print(f"na face {i} saiu {lista4[i]} vezes")









