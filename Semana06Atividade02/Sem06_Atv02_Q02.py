contador = 0
media = 0
total = 0
maior = 0
menor = 0
while True:
    n = int(input("Digite sua idade: "))
    if n == 0: break
    contador += 1
    total += n
    media = total // contador
    if contador == 1:
        maior = menor = n
    if maior < n :
        maior = n
    if menor > n :
        menor = n


print(f'O numero de participantes do grupo é de  {contador} pessoas, A idade media do grupo é de {media} anos, A maior idade é {maior} anos e a menor é {menor} anos')



