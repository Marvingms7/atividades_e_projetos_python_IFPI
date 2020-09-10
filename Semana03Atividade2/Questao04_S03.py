def e_letra_numero(a):
    return a in 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTUuVvWwXxYyZz0123456789'

def main():
    a = str(input("Digite uma consoante, vogal ou um numero entre 0 e 9: "))
    resultado = e_letra_numero(a)
    print(f'{a} faz parte do alfabeto ou esta entre 0 e 9? {resultado}  ')

if __name__ == '__main__':
    main()