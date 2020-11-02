alfabeto = "abcdefghijklmnopqrstuvwxyz"
letra = input("Por favor, entre com uma letra para criptografar: ")
chave = int(input("Digite a chave numérica que desejar: "))
posicao = alfabeto.find(letra)
novaPosicao = (posicao + chave) % 26
letraCriptografada = alfabeto[novaPosicao]
print("Sua letra criptografada é", letraCriptografada)
