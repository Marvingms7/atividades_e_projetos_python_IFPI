print('''1 - De onde é a invenção do chuveiro elétrico?
a) França
b) Inglaterra
c) Brasil
d) Austrália
e) Itália
''')
resposta1 = str(input("Qual a alternativa correta? "))
print('''2 - Qual o número mínimo de jogadores numa partida de futebol?
a) 8
b) 10
c) 9
d) 5
e) 7
''')
resposta2 = str(input("Qual a alternativa correta? "))
print('''3 - Qual o maior animal terrestre?
a) Baleia Azul
b) Dinossauro
c) Elefante africano
d) Tubarão Branco
e) Girafa
''')
resposta3 = str(input("Qual a alternativa correta? "))
print('''4 - De quem é a famosa frase “Penso, logo existo”?
a) Platão
b) Galileu Galilei
c) Descartes
d) Sócrates
e) Francis Bacon
''')
resposta4 = str(input("Qual a alternativa correta? "))
print('''5 -  Quais o menor e o maior país do mundo?
a) Vaticano e Rússia
b) Nauru e China
c) Mônaco e Canadá
d) Malta e Estados Unidos
e) São Marino e Índia
''')
resposta5 = str(input("Qual a alternativa correta? "))
print('''6. Qual o grupo em que todas as palavras foram escritas corretamente?
a) Asterístico, beneficiente, meteorologia, entertido
b) Asterisco, beneficente, meteorologia, entretido
c) Asterisco, beneficente, metereologia, entretido
d) Asterístico, beneficiente, metereologia, entretido
e) Asterisco, beneficiente, metereologia, entretido
''')
resposta6 = str(input("Qual a alternativa correta? "))
print('''7. Qual o livro mais vendido no mundo a seguir à Bíblia?
a) O Senhor dos Anéis
b) Dom Quixote
c) O Pequeno Príncipe
d) Ela, a Feiticeira
e) Um Conto de Duas Cidades
''')
resposta7 = str (input("Qual a alternativa correta? "))
print('''8. Quantas casas decimais tem o número pi?
a) Duas
b) Centenas
c) Infinitas
d) Vinte
e) Milhares
''')
resposta8 = str(input("Qual a alternativa correta? "))
print('''9. Atualmente, quantos elementos químicos a tabela periódica possui?
a) 113
b) 109
c) 108
d) 118
e) 92
''')
resposta9 = str(input("Qual a alternativa correta? "))
print('''10. Quais os principais autores do Barroco no Brasil?
a) Gregório de Matos, Bento Teixeira e Manuel Botelho de Oliveira
b) Miguel de Cervantes, Gregório de Matos e Danthe Alighieri
c) Padre Antônio Vieira, Padre Manuel de Melo e Gregório de Matos
d) Castro Alves, Bento Teixeira e Manuel Botelho de Oliveira
e) Álvares de Azevedo, Gregório de Matos e Bento Teixeira
''')
resposta10 = str(input("Qual a alternativa correta? "))

score = 0
if resposta1 == "c":
    score = 1
if resposta2 == "e":
    score += 1
if resposta3 == "c":
    score += 1
if resposta4 == "c":
    score += 1
if resposta5 == "a":
    score += 1
if resposta6 == "b":
    score += 1
if resposta7 == "b":
    score += 1
if resposta8 == "c":
    score += 1
if resposta9 == "d":
    score += 1
if resposta10 == "a":
    score += 1
if score == 10:
    print(f'Parabéns, você acertou todas!!!')
elif score == 5:
    print(f'Você acertou metade da questões, tente novamente!')
elif score == 6:
    print(f'Legal, você acertou mais da metade, tente novamente!')
elif score == 8:
    print(f'Muito bom, por 2 questões você acertava todas, tente novamente!')
elif score == 9:
    print(f'Espetacular, você só errou 1 questão, tente novamente!')
else:
    print(f'Você acertou menos da metade, estude um pouquinho mais e tente novamente!')


print(f'Você fez um total de {score} pontos')











