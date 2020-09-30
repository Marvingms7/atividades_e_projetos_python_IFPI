v_carro = float(input("Informe o valor: "))
total_mes_carro = (0.004 * v_carro) +v_carro
p_inicial = 10000
renda_total = (0.007 * p_inicial) + p_inicial
mes = -1
while True:
    mes += 1
    total_mes_carro = (0.004 * total_mes_carro) + total_mes_carro
    if renda_total < total_mes_carro:
        renda_total = (0.007 * renda_total) + renda_total
    else:
        break

print(f'Você so podera comprar um carro com {mes} meses!')