soma = 0
for k in range(0, 100):
    #entrada
    a = int(input("Digite um numero: "))
    #Processamento
    soma = a + soma
    media = soma / 100
#Saida
print(f'a media é {media:.2f}')