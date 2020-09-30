a = int(input("Digite a população do país A: "))
b = int(input("Digite a população do país B: "))
natalidade1 = (0.02 * a) + a
natalidade2 = (0.03 * b) + b
acumulador = 0
while True:
    acumulador += 1
    if natalidade1 > natalidade2:
        natalidade1 = (0.02 * natalidade1) + natalidade1
        natalidade2 = (0.03 * natalidade2) + natalidade2
    else:
        natalidade1 = (0.03 * a) + a
        natalidade2 = (0.02 * b) + b
        while natalidade2 > natalidade1:
            acumulador += 1
            natalidade1 = (0.03 * natalidade1) + natalidade1
            natalidade2 = (0.02 * natalidade2) + natalidade2
        else:break

if a > b:
    print(f'A população "B" sera maior que a "A" em {acumulador} anos.')
else:
    print(f'A população "A" sera maior que a "B" em {acumulador} anos.')







