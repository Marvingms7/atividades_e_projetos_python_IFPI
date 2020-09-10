n1 = float(input("Digite a altura: "))
n2 = float(input("Digite o comprimento: "))
n3 = float(input("Digite o valor da largura: "))
area = n3 * n2
volume = n1 * n2 * n3
area_parede = (2 * n1 * n3) + (2 * n1 * n2)
print( f' a área do piso da sala é de {area} metros quadrados, o volume é {volume} metros cúbicos e a área das paredes é {area_parede} metros quadrados.')