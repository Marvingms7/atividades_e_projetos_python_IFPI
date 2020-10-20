textSpeakDictionary = {
    "rs" : "risos",
    "tbm" : "também",
    "vc" : "você",
    "pdc" : "pode crer",
    "vdc" : "vai da certo",
    "mds" : "meu Deus",
    "plmd" : "pelo amor de deus",
    "flw" : "falou",
    "vlw" : "valeu",
    "tlgd" : "ta ligado",
    "sqn" : "só que não",
    "dmr" : "demorou"
}
sentence = input("Insira uma frase para traduzir: ").lower()
wordsToTranslate = sentence.split()
translatedSentece = ""

for word in wordsToTranslate:
    if word in textSpeakDictionary:
        translatedSentece += textSpeakDictionary[word] + " "
    else:
        translatedSentece += word + " "

print("==>")
print(translatedSentece)