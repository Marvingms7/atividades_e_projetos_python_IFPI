listA = []
listB = []
listC = []
indice = 0
for i in range(1, 21):
    n = int(input())
    listA.append(n)
for c in range(1, 21):
    n2 = int(input())
    listB.append(n2)
while indice < len(listA):
    listC.append(listA[indice] + listB[indice])
    indice += 1
print(f'{listA}\n{listB}\n{listC}')