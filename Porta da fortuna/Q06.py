from random import *
tentativas = 0
score = 0
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
while score < 3:
    tentativas += 1
    print(f'\nTentativa {tentativas}: Escolha uma porta (1, 2, 3): ')
    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)
    portaCerta = randint(1,3)
    print(f'A porta escolhida foi a {portaEscolhida}')
    print(f'A porta certa é, {portaCerta}')
    if portaEscolhida == portaCerta:
        print(f'Parabéns!')
        score += 1
    else:
        print(f'Que peninha!')
    print(f'Sua pontuação é {score}')
print(f'\n** Você conseguiu! Terminou o jogo em {tentativas} tentativas **')
