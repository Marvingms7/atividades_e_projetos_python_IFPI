def segundos_em_horas(a):
    horas = a // (60 * 60)
    minutos = (a % 3600) // 60
    segundos = (a % 3600) % 60
    return print(f'{horas}:{minutos}:{segundos}')

def main():
    segundos_em_horas(a)

a = int(input("Digite o numero de segundos: "))

if __name__ == '__main__':
    main()