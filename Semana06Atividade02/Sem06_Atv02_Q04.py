print('''   CODIGO    PRODUTO        PREÇO (R$)
      H      HAMBURGUER      5.50
      C      CHEESEBURGUER   6.80
      M      MISTO QUENTE    4.50
      A      AMERICANO       7.00
      Q      QUEIJO PRATO    4.00
      X      PARA TOTAL DA COMPRA
      ''')

compra = str(input("Digite a letra inicial do item que vai ser adquirido: ")).upper()[0]
contador = 0
total = 0
valor = 0
while True:
    contador += 1
    if compra == 'X': break
    elif compra == 'H':
        valor += 5.50
    elif compra == 'C':
        valor += 6.80
    elif compra == 'M':
        valor += 4.50
    elif compra == 'A':
        valor += 7.00
    elif compra == 'Q':
        valor += 4.00
    elif compra != 'hcmaqx':
            print(f' codigo invalido')
    total = valor
    compra = str(input("Digite a letra inicial do item que vai ser adquirido: ")).upper()[0]

print(f'O valor total é de {total:.2f} R$')







