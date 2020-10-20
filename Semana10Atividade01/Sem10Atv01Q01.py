livros = {
    }
def adicionar_livro():
    contador = 0
    while True:
        codigo = 101 + contador
        titulo = input("Digite o titulo do livro: ").strip()
        if titulo == '':
            break
        isbn = (input("Digite a ISBN: ")).strip()
        autor = input("Digite o autor: ").strip()
        preco = float(input("Digite o preço: "))
        livro = (titulo, isbn, autor, preco)
        livros[codigo] = livro
        contador += 1


def codigo(livros):
    for i in livros.keys():
        titulo, isbn, autor, preco, = livros[i]
        print(f'Código: {i}\nTítulo: {titulo}\nISBN: {isbn}\nAutor: {autor}\nPreço: {preco:.2f}')


def main():
    adicionar_livro()
    codigo(livros)

if __name__ == '__main__':
    main()
