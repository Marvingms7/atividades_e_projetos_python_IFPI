vogais_consoantes = {}
def text():
    texto = input().strip().upper()
    for c in '\n,.`´^:;><?!@#$*-=_()':
        texto = texto.replace(c, "")
    for i in texto:
        if i in'ÀÁÂÃAÉÊÈÎÍÌÚÙÛÔÓÒÕBCÇDEFGHIJKLMNOPQRSTUVWXYZ':
            if i in 'ÁÀÂÃ':
                i = 'A'
            elif i in 'ÉÊÈ':
                i = 'E'
            elif i in 'ÎÍÌ':
                i = 'I'
            elif i in 'ÔÓÒÕ':
                i = 'O'
            elif i in 'ÚÙÛ':
                i = 'U'
            elif i == 'Ç':
                i = 'C'
            if i in vogais_consoantes:
                vogais_consoantes[i] += 1
            else:
                vogais_consoantes[i] = 1

    print(f'{vogais_consoantes}')

def main():
    text()



if __name__ == '__main__':
    main()





