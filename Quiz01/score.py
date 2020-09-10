print('''1 - Qual a religião monoteísta que conta com o maior número de adeptos no mundo?
a) Judaísmo
b) Zoroastrismo
c) Islamismo
d) Cristianismo
e) Hinduísmo
''')
resposta01 = str(input("Digite a alternativa correta: "))
print('''1 - Qual desses filmes foi baseado na obra de Shakespeare?
a) Muito Barulho por Nada (2012)
b) Capitães de Areia (2011)
c) A Dama das Camélias (1936)
d) A Revolução dos Bichos (1954)
e) Excalibur (1981)
''')
resposta02 = str(input("Digite a alternativa correta: "))
print('''1 - Quem foi o primeiro homem a pisar na Lua? Em que ano aconteceu?
a) Yuri Gagarin, em 1961
b) Buzz Aldrin, em 1969
c) Charles Conrad, em 1969
d) Charles Duke, em 1971
e) Neil Armstrong, em 1969
''')
resposta03 = str(input("Digite a alternativa correta: "))
print('''1 - Qual o nome do cientista que descobriu o processo de pasteurização e a vacina contra a raiva?
a) Marie Curie
b) Blaise Pascal
c) Louis Pasteur
d) Antoine Lavoisier
e) Charles Darwin
''')
resposta04 = str(input("Digite a alternativa correta: "))
print('''1 - As pessoas de qual tipo sanguíneo são consideradas doadores universais?
a) Tipo A
b) Tipo B
c) Tipo O
d) Tipo AB
e) Tipo ABO
''')
resposta05 = str(input("Digite a alternativa correta: "))
print('''1 - Quais são os cromossomos que determinam o sexo masculino?
a) Os V
b) Os X
c) Os Y
d) Os W
e) Os Z
''')
resposta06 = str(input("Digite a alternativa correta: "))
print('''1 - Em que estado australiano fica situada a cidade de Sydney?
a) Nova Gales do Sul
b) Victoria
c) Tasmânia
d) Queensland
e) Norfolk
''')
resposta07 = str(input("Digite a alternativa correta: "))
print('''1 - Como se chamam os vasos que transportam sangue do coração para a periferia do corpo?
a) veias
b) átrios
c) ventrículos
d) artérias
e) aurículos
''')
resposta08 = str(input("Digite a alternativa correta: "))
print('''1 - Com que dois países faz fronteira o Equador?
a) com o Brasil e com a Colômbia
b) com a Colômbia e com a Venezuela
c) com a Colômbia e com o Peru
d) com o Peru e com o Equador
e) com o Equador e o Brasil
''')
resposta09 = str(input("Digite a alternativa correta: "))
print('''1 - Qual é o maior arquipélago da Terra?
a) a Filipinas
b) a Indonésia
c) as Bahamas
d) a Finlândia
e) as Maldivas
''')
resposta10 = str(input("Digite a alternativa correta: "))

score = 0

if resposta01 == "d":
    score = 1
if resposta02 == "a":
    score += 1
if resposta03 == "e":
    score += 1
if resposta04 == "c":
    score += 1
if resposta05 == "c":
    score += 1
if resposta06 == "c":
    score += 1
if resposta07 == "a":
    score += 1
if resposta08 == "d":
    score += 1
if resposta09 == "c":
    score += 1
if resposta10 == "a":
    score += 1

print(f'Você fez {score} pontos!)')

