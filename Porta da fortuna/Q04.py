from random import *
jogando = True
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
while jogando == True:
    print("\nEscolha uma porta (1, 2, ou 3): ")
    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)
    portaCerta = randint(1,3)
    print(f'A porta escolhida é a porta {portaEscolhida}')
    print(f'A porta certa é a porta {portaCerta}')
    if portaEscolhida == portaCerta:
        print(f'Parabens!')
        score += 1
    else:
        print(f'Que peninha!')
    print(f'Sua pontuação é {score}')
    print(f'\nVocê quer jogar de novo?(S/N)')
    resposta = input().upper()
    if resposta == 'N' or resposta == 'nao':
        jogando = False
    print(f'Obrigado por jogar!')
    print(f'Sua pontuação final é de {score}')