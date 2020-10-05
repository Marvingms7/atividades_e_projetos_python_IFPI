from random import*
nome = str(input("Qual o seu nome? "))

executar = True
adjetivos = ["maravilhoso", "acima da média", "excelente", "incrivel", "admirável", "brilhante", "destemido", "dedicado", "disposto", "desenrolado","eficiente", "efusivo", "esplêndido", "esplendoso", "evoluido", "exemplar", "experiente", "extraordinario", "exuberante", "encantador", "engenhoso", "forte", "fabuloso", "fascinante", "firme", "fenomenal", "formidavel", "fervoroso", "gracioso", "gênio", "glorioso", "glamoroso", "gigantesco", "honroso"]
hobbies = ["andar de bicicleta", "programar", "cozinhar", "jogar video games", "praticar esportes", "dançar", "costruir algo", "fazer tricô", "patinar", "andar de skate", "pilotar kart", "jogar league of legends", "jogar CS.go", "jogar Valorant", "jogar Dota online 2", "Fotografar", "trabalhar com ediçoes", "jogar futebol", "Decorar", "pintar", "desenhar", "praticar musculação"]
print('''
Menu
   c = obter cumprimento
   a = adicionar hobby
   d = remover hobby
   p = imprimir hobbies
   q = sair
''')

while executar == True:
    menuChoice = input("\n_").lower()

    if menuChoice == 'c':
        print("Aqui está o seu cumprimento", nome,":" )
        print(nome,"você é", choice(adjetivos), "em", choice(hobbies))
        print("De nada!")
    elif menuChoice == 'a':
        itemToAdd = input("Adicione o hobby: ")
        if itemToAdd not in hobbies:
            hobbies.append(itemToAdd)
            print("hobby adicionado com sucesso!")
        else:
            print("O hobby não foi adicionado, pois ja está na lista")
    elif menuChoice == 'd':
        itemToDelete = input("insira o hobby a ser removido: ")
        if itemToDelete in hobbies:
            hobbies.remove(itemToDelete)
            print("hobby removido com sucesso!")
        else:
            print(f'O hobby não está na lista!')
    elif menuChoice == 'p':
        print(hobbies)
    elif menuChoice == 'q':
        executar = False
    else:
        print("Insira uma opção válida!")
