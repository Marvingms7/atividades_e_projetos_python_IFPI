from random import *
acumulador = 0
jogando = True
print('''
Vinte e um!
========
Tente fazer exatamente 21 pontos!
''')
while jogando == True:
    numAleatorio = randint(1, 10)
    acumulador += numAleatorio
    print(f'Seu proximo numero é {numAleatorio}')
    print(f'Sua pontuação agora é {acumulador}')
    print(f'Gostaria de somar mais um numero? (S/N): ')
    resposta = input().upper()
    if resposta == 'N' or resposta == 'nao':
        jogando = False
print(f'Sua pontuação final é {acumulador}')
if acumulador == 21:
    print(f'Você venceu, Parabéns!!!')
else:
    print(f'Não foi dessa vez, Que peninha!')








