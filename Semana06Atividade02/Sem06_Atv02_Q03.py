print('''OPÇÕES:\n1-SAUDAÇÕES\n2-BRONCA\n3-FELICITAÇÃO\n0-FIM
''')
op1 = int(input("Digite o numero da sua opção: "))
while op1 != 0:
    if op1 != 1 or op1 != 2 or op1 != 3:
        op1 = 0
        print('Opção invalida.')

    if op1 == 1:
        print(f'Olá. Como vai?')
        print('''OPÇÕES:\n1-SAUDAÇÕES\n2-BRONCA\n3-FELICITAÇÃO\n4-FIM
        ''')
        op1 = int(input("Digite o numero da sua opção: "))
    if op1 == 2:
        print(f'Vamos estudar mais.')
        print('''OPÇÕES:\n1-SAUDAÇÕES\n2-BRONCA\n3-FELICITAÇÃO\n4-FIM
        ''')
        op1 = int(input("Digite o numero da sua opção: "))
    if op1 == 3:
        print(f'Meus Parabéns!')
        print('''OPÇÕES:\n1-SAUDAÇÕES\n2-BRONCA\n3-FELICITAÇÃO\n4-FIM
        ''')
        op1 = int(input("Digite o numero da sua opção: "))
    if op1 == 0: break

print(f'Fim de Serviço.')
