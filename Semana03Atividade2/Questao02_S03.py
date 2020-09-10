def e_letra(a):
    return a in 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTUuVvWwXxYyZz'

def main():
    a = str(input("Digite uma consoante ou vogal: "))
    resultado = e_letra(a)
    print(f'{a} é faz parte do alfabeto? {resultado}  ')

if __name__ == '__main__':
    main()