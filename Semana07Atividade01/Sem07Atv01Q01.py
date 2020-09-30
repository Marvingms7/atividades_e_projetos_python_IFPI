n = int(input("Digite a quantidade de metros: "))
while True:
    metros = 500
    tempo_total = (((n // metros) * 60) + n) // 10
    resultado = tempo_total
    print(f'A lebre ultrapassara a tartaruga em {resultado} minutos')
    print(f'Deseja continuar testando o programa a ou não, digite (S/N)? ')
    r = input().lower()
    if r == 's':
        n = int(input("Digite a quantidade de metros: "))
    else:
        if r == 'n': break
print(f'Obrigado por participar!')

