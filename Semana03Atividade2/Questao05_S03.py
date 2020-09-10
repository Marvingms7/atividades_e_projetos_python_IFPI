def e_s(s):
    if s in 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTVvWwXxYyZz':
       print(f'Consoante')
    elif s in 'AaEeIiOoUu':
        print(f'Vogal')
    elif s in 'Çç"!@#$%¨&*()_+.+-*/<>:?^`{}︰''´[~.,;/':
       print(f'Simbolo')
    else:
       print(f'Numero')

def main():
    s = str(input("Digite um caractere: "))
    resultado = e_s(s)
    f'{resultado}'

if __name__ == '__main__':
    main()