from random import *
print('''
Porta da fortuna!
=========
Existe um grande premio atrás de uma dessas 3 portas!
Advinhe qual a porta certa pra ganhar o prêmio!
 _______   _______   _______
|       | |       | |       |
| [ 1 ] | | [ 2 ] | | [ 3 ] |
|     o | |     o | |     o |
|       | |       | |       |
|_______| |_______| |_______|
''')
for attempt in range(3):
    print(f'\nEscolha uma porta (1, 2, 3): ')
    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)
    portaCerta = randint(1,3)
    print(f'A porta escolhida foi,{portaEscolhida}')
    print(f'A porta certa é, {portaCerta}')
    if portaEscolhida == portaCerta:
        print(f'Parabéns, você acertou a porta!')
    else:
        print(f'Você errou, que peninha!')
