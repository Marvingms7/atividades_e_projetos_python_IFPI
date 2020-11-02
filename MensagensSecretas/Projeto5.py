alfabeto = "zdbcefghijwloumpqsrtnvkxya"
letra = input("Por favor, entre com uma letra para criptografar: ").lower()
chave = int(input("Digite a chave numerica que desejar: "))
letraCriptografada = ''
for i in letra:
    if i in alfabeto:
        posicao = alfabeto.lower().find(i)
        novaPosicao = (posicao + chave) % 26
        letraCriptografada += alfabeto[novaPosicao]
        chave += 1
    else:
        letraCriptografada = letraCriptografada + i
print("Sua letra criptografada é", letraCriptografada)