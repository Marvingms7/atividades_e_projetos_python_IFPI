from random import*
print("Gerador de cumprimentos")
print("--------------------")

adjetivos = ["maravilhoso", "acima da média", "excelente", "incrivel", "admirável", "brilhante", "destemido", "dedicado", "disposto", "desenrolado","eficiente", "efusivo", "esplêndido", "esplendoso", "evoluido", "exemplar", "experiente", "extraordinario", "exuberante", "encantador", "engenhoso", "forte", "fabuloso", "fascinante", "firme", "fenomenal", "formidavel", "fervoroso", "gracioso", "gênio", "glorioso", "glamoroso", "gigantesco", "honroso"]
hobbies = ["andar de bicicleta", "programar", "cozinhar", "jogar video games", "praticar esportes", "dançar", "costruir algo", "fazer tricô", "patinar", "andar de skate", "pilotar kart", "jogar league of legends", "jogar CS.go", "jogar Valorant", "jogar Dota online 2", "Fotografar", "trabalhar com ediçoes", "jogar futebol", "Decorar", "pintar", "desenhar", "praticar musculação"]

nome = input("Qual é o seu nome?: ")
print("Aqui está o seu cumprimento", nome, ":")
print(nome, "você é", choice(adjetivos), "em", choice(hobbies))
print("De nada!")