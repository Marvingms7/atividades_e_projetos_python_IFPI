print('Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue? \n a) Tem entre 2 a 4 litros. São retirados 450 mililitros. \n b) Tem entre 4 a 6 litros. São retirados 450 mililitros. \n c) Tem 10 litros. São retirados 2 litros. \n d) Tem 7 litros. São retirados 1,5 litros. \n e) Tem 0,5 litros. São retirados 0,5 litros. \n resposta:' )
resposta = input().lower()
if resposta == "b":
    print(":) PARABÉNSSS, você acertou!!! 	^_^  ")
elif resposta == "a":
    print(':( não foi desta vez')

elif resposta == "c":
    print('Você errou bobinho(a) ¯\_(ツ)_/¯')
elif resposta == "d":
    print(':’( Você pode tantar quantas vezes quiser! ')
elif  resposta  ==  "e" :
    print ( 'Não fique triste, você pode tentar mais vezes! ಠ_ಠ' )    
    
else:
    print('Você não selecionou a, b, c, d ou ae, tente novamente!!')

