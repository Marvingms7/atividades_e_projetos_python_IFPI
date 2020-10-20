def displayMenu():
    print("tradutor de expressões")
    print("=" * 13)
    print("menu:")
    print(" c = converter uma frase")
    print(" p = imprimir dicionario")
    print(" a = adicionar uma palavra")
    print(" d = remover uma palavra")
    print(" q = sair")

def convertSentece():
    sentece = input("Insira uma frase para traduzir: ").lower()
    translatedSentece = ""
    listOfWords = sentece.split()
    for char in '?!.,':
        sentece = sentece.replace(char,'')
    listOfWords = sentece.split()
    for word in listOfWords:
        if word in textSpeakDictionary:
            translatedSentece += textSpeakDictionary[word] + " "
        else:
            translatedSentece += word + " "
    print("==>")
    print(translatedSentece)
def addDictionaryItem():
    txtToAdd = input("Insira a expressão a ser adicionada ao dicionario: ")
    if txtToAdd not in textSpeakDictionary:
        meaning = input("O que ela sgnifica?: ")
        textSpeakDictionary[txtToAdd] = meaning
    else:
        print(f'A expressão ja existe no dicionario')
def deleteDictionaryItem():
    txtToDelete = input("Insira a expressão a ser removida ao dicionario: ")
    if txtToDelete not in textSpeakDictionary:
        print(f'Não foi possivel deletar, essa expressão nao existe no dicionario')
    else:
        del textSpeakDictionary[txtToDelete]


textSpeakDictionary = {
    "rs": "risos",
    "tbm": "também",
    "vc": "você",
    "pdc": "pode crer",
    "vdc": "vai da certo",
    "mds": "meu Deus",
    "plmd": "pelo amor de deus",
    "flw": "falou",
    "vlw": "valeu",
    "tlgd": "ta ligado",
    "sqn": "só que não",
    "dmr": "demorou"
}
running = True
displayMenu()
while running == True:
    menuChoice = input(">_").lower()
    if menuChoice == 'c':
        convertSentece()
    elif menuChoice == 'p':
        print(textSpeakDictionary)
    elif menuChoice == 'a':
        addDictionaryItem()
    elif menuChoice == 'd':
        deleteDictionaryItem()
    elif menuChoice == 'q':
        running = False
    else:
        print("Escolha invalida")

