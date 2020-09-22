nota = float(input('Digite sua nota, Valor entre "0 e 10": '))
while True:
    if nota >= 8.5 and nota <= 10:
        print('Nota igual a A')
    elif nota >= 7.0 and nota <= 8.4:
        print('Nota igual a B')
    elif nota >= 5.0 and nota <= 6.9:
        print('Nota igual a C')
    elif nota >= 4.0 and nota <= 4.9:
        print('Nota igual a D')
    elif nota >= 0 and nota <= 3.9:
        print('Nota igual a E')
    else:
        print('Nota invalida')
    nota = float(input('Digite sua nota, Valor entre "0 e 10": '))






