def sinal(c):
    if c == "v":
        return f'Siga!'
    elif c == "a":
        return f'Atenção!'
    elif c == "e":
        return f'Pare!'

def main():
    c = input('Digite uma cor, "v"" é verde, "a" é amarelo e "e" é vermelho: ')
    resultado = sinal(c)
    print(f'{resultado}')

if __name__ == '__main__':
    main()
