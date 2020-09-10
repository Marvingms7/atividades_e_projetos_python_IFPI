def o_signo(a, b):
    if a == 3:
        if b <= 20:
            return f'Peixes'
        else:
            return f'Aries'
    elif a == 4:
        if b <= 19:
            return f'Aries'
        else:
            return f'Touro'
    elif a == 5:
        if b <= 20:
            return f'Touro'
        else:
            return f'Gemeos'
    elif a == 6:
        if b <= 21:
            return f'Gemeos'
        else:
            return f'Cancer'
    elif a == 7:
        if b <= 22:
            return f'Cancer'
        else:
            return f'Leão'
    elif a == 8:
        if b <= 22:
            return f'Leão'
        else:
            return f'Virgem'
    elif a == 9:
        if b <= 22:
            return f'Virgem'
        else:
            return f'Libra'
    elif a == 10:
        if b <= 22:
            return f'Libra'
        else:
            return f'Escorpião'
    elif a == 11:
        if b <= 21:
            return f'Escorpião'
        else:
            return f'Sargitario'
    elif a == 12:
        if b <= 21:
            return f'Sargitario'
        else:
            return f'Capricornio'
    elif a == 1:
        if b <= 19:
            return f'Capricornio'
        else:
            return f'Aquario'
    elif a == 2:
        if b <= 18:
            return f'Aquario'
        else:
            return f'Peixes'
    elif a == 3:
        if b <= 20:
            return f'Peixes'
        else:
            return f'Aries'


def main():
    mes = int(input("Digite o mês do seu aniversario: "))
    dia = int(input("Digite o dia do seu aniversario: "))
    resultado = o_signo(mes, dia)
    print(f'{resultado}')


if __name__ == '__main__':
    main()
