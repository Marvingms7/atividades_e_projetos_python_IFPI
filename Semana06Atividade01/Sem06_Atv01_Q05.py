salario = int(input("Digite seu salario: "))
divida = int(input("Digite o valor da divida: "))
ano = 0
mes = 0
salario_total = 0
divida_total = 0
while True:
    if salario > divida:
        mes += 1
        salario_total += salario
        divida_total += (divida * 15) / 100 + divida
    if divida_total > salario_total: break
    if mes == 3:
        salario_total += (salario * 5) / 100 + salario
    if mes == 12:
        ano = mes = 1
print(f'{salario_total} {divida_total} {mes} {ano}')




