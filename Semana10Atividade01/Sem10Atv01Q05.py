dadosTotal = {}
def notas():
    while True:
        matricula = input("Digite sua matricula: ")
        if matricula == '':
            break
        nome = input("Digite seu nome: ")
        nota1 = float(input("Digite a sua nota: "))
        nota2 = float(input("Digite a sua segunda nota: "))
        dados = nome, nota1, nota2
        dadosTotal[matricula] = dados

def resultado_media():
    while True:
        matriculaMedia = input("Digite sua matricula para saber a media: ")
        if matriculaMedia == '':
            break
        if matriculaMedia not in dadosTotal:
            print(f'Matricula invalida!')
        for i in dadosTotal:
            if matriculaMedia == i:
                nome, nota1, nota2 = dadosTotal[matriculaMedia]
                media = (nota1 + nota2) / 2
                print(f'{nome} {media:.1f}')



def main():
    notas()
    resultado_media()
if __name__ == '__main__':
    main()


    