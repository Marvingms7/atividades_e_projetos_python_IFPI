alfabeto = "abcdefghijklmnopqrstuvwxyz"
letra = input("Por favor, entre com uma letra para criptografar: ").lower()
chave = int(input("Digite a chave numerica que desejar: "))
letraCriptografada = ''
if chave == 12 and letra != 'd' and letra != 'x':
    for i in letra:
        if i in alfabeto:
            posicao = alfabeto.lower().find(i)
            novaPosicao = (posicao - chave) % 26
            letraCriptografada += alfabeto[novaPosicao]
        else:
            letraCriptografada = letraCriptografada + i
    print("Sua letra criptografada é", letraCriptografada)

elif letra == 'd':
    chave = 7
    posicao = alfabeto.find(letra)
    novaPosicao = (posicao + chave) % 26
    letraCriptografada = alfabeto[novaPosicao]
    print("Sua letra criptografada é", letraCriptografada)
elif letra == 'x':
    chave = 4
    posicao = alfabeto.find(letra)
    novaPosicao = (posicao + chave) % 26
    letraCriptografada = alfabeto[novaPosicao]
    print("Sua letra criptografada é", letraCriptografada)

