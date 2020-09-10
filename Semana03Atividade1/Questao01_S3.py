def resultado(nome, sexo):
    if sexo == 1:
        return print(f'Ilmo Sr.{nome}')
    if sexo == 2:
        return print(f'Ilmo Sra.{nome}')

def main():
    resultado(nome, sexo)

n1 = input("Digite seu nome: ")
n2 = int(input("Digite seu sexo, se for masculino digite 1, feminio digite 2: "))

nome = n1
sexo = n2

if __name__ == '__main__':
   main()