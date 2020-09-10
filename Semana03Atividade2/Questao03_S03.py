def e_consoante(n):
    return n in 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTVvWwXxYyZz'



def main():


   n = str(input("Digite uma consoante: "))
   resultado = e_consoante(n)
   print(f'"{n}" é consoante? {resultado}')

if __name__ == '__main__':
    main()