def e_vogal(n):
    return n in 'AaEeIiOoUu'



def main():


   n = str(input("Digite uma vogal: "))
   resultado = e_vogal(n)
   print(f'"{n}" é volgal? {resultado}')

if __name__ == '__main__':
    main()

