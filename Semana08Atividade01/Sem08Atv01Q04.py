listTotal = []
listPar = []
listImpar = []
for c in range(1, 21):
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        listTotal.append(n)
        listPar.append(n)
    else:
        listImpar.append(n)
        listTotal.append(n)
print(f'{listTotal}\n{listPar}\n{listImpar}')