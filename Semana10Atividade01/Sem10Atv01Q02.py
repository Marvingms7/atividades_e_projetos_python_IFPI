listaTel = {}
def info(a):
    codigo = 0
    contador = 0
    for c in range(0, a):
        codigo  = 1 + contador
        nome = input().strip()
        cidade = input().strip()
        estado = input().strip()
        telefone = (input()).strip()
        dados = nome, cidade, estado, telefone
        listaTel[codigo] = dados
        contador += 1

def organizar(listaTel):
    for k, i in listaTel.items():
        nome, cidade, estado, telefone = listaTel[k]
        print(f'{nome:<20} {cidade:}({estado}){telefone:}\n',end='')



def main():
    n = int(input())
    resultado = info(n)
    organizar(listaTel)

if __name__ == '__main__':
    main()