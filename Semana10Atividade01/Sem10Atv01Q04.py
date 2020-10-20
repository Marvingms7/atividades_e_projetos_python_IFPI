vogais = {}
def text():
    contador1 = 0
    contador2 = 0
    contador3 = 0
    contador4 = 0
    contador5 = 0
    letra1 = letra2 = letra3 = letra4 = letra5 = 0
    texto = input().strip()
    for i in texto:
        if i.lower() in 'aeiouàáãâèéêìíòóô':
            if i.lower() == 'a' or i == 'ã' or i == 'á' or i == 'à':
                contador1 += 1
            if i.lower() == 'e' or i == 'é' or i == 'ê':
                contador2 += 1
            if i.lower() == 'i' or i == 'ì' or i == 'í':
                contador3 += 1
            if i.lower() == 'o' or i == 'ò' or i == 'ô' or i == 'õ' or i == 'ó':
                contador4 += 1
            if i.lower() == 'u' or i == 'ù' or i == 'ú':
                contador5 += 1

    print(f'A: {contador1}\nE: {contador2}\nI: {contador3}\nO: {contador4}\nU: {contador5}')

def main():
    text()



if __name__ == '__main__':
    main()







