from random import*
executar = True
contador = 0
nomesMasculinos = ["Thor", "Zeus", "floquinhos", "luke", "Apolo", "Sheik", "Luke", "Bolota", "Nick", "Boris", "Charlie", "Eros", "Zé", "theo", "Tobby", "Barth", "Totó", "billy", "bradoq", "Scott", "Duque", "Toddy", "Dexter", "Brutus", "spike", "Chico", "Chiquinhos", "Zeca", "Loki", "Nico", "Frederico", "Bidu", "Pipoca", "Biscoito", "Bartholomeu", "Tobias"]
nomesFeminino = ["Mel", "Lili", "Chloé", "Perola", "Shakira", "Lara", "Valentina", "Mia", "Lady", "Maggie", "Maya", "Lucy", "Juju", "Laika", "Lolla", "Hannah", "Bebel", "pandora", "Marie", "julie", "Vicky", "Bela", "Princesa", "Fiona", "Madonna", "kiara", "Cristal", "Ruby", "Sophie", "Angel", "Marry", "Tiffany", "Tequila", "Teka", "Marry", "Duda", "Mila", "Eva"]
nomes_p_qualquer_animal_maculino = ['Lucky', 'Luke', 'Lord', 'Martin', 'Nick', 'Nico', 'Oliver', 'Orpheu', 'Pablo', 'Paco', 'Pancho','Quico', 'Quixote', 'Rabugento', 'Radar', 'Rex', 'Red', 'Rick', 'Salomão', 'Salomé', 'Sam', 'Trovão', 'Tubarão', 'Tutti', 'Twiggy', 'Twister','Tango', 'Tarot', 'Tarzan', 'Ubaldo', 'Uriel', 'Urso', 'Uggy', 'Ulisses', 'Veloz', 'Vlad',  'Valente', 'Xandi', 'Xarope', 'York', 'Yoshi', 'Young', 'Yoyo']
nomes_p_qualquer_animal_feminino = ['Lady', 'Lana', 'Lola', 'Lilica', 'Laila', 'Linda', 'Lolita', 'Mafalda', 'Meg', 'Mel', 'Minnie', 'Mona', 'Molly', 'Oddie', 'Ohana', 'Pandora', 'Pérola', 'Pink', 'Pedrita', 'Pitty', 'Rubi', 'Rayssa', 'Xulica', 'Xuxa', 'Xuxu', 'Xaila', 'Yanca', 'Yasmim', 'Juju', 'Julie', 'June', 'Emília', 'Emily', 'Duda', 'Duquesa', 'Barbie', 'Atena', 'Alice', 'Amora']
nomes_total = ['Lucky', 'Luke', 'Lord', 'Martin', 'Nick', 'Nico', 'Oliver', 'Orpheu', 'Pablo', 'Paco', 'Pancho','Quico', 'Quixote', 'Rabugento', 'Radar', 'Rex', 'Red', 'Rick', 'Salomão', 'Salomé', 'Sam', 'Trovão', 'Tubarão', 'Tutti', 'Twiggy', 'Twister','Tango', 'Tarot', 'Tarzan', 'Ubaldo', 'Uriel', 'Urso', 'Uggy', 'Ulisses', 'Veloz', 'Vlad',  'Valente', 'Xandi', 'Xarope', 'York', 'Yoshi', 'Young', 'Yoyo', 'Lady', 'Lana', 'Lola', 'Lilica', 'Laila', 'Linda', 'Lolita', 'Mafalda', 'Meg', 'Mel', 'Minnie', 'Mona', 'Molly', 'Oddie', 'Ohana', 'Pandora', 'Pérola', 'Pink', 'Pedrita', 'Pitty', 'Rubi', 'Rayssa', 'Xulica', 'Xuxa', 'Xuxu', 'Xaila', 'Yanca', 'Yasmim', 'Juju', 'Julie', 'June', 'Emília', 'Emily', 'Duda', 'Duquesa', 'Barbie', 'Atena', 'Alice', 'Amora']
print('''
Menu:
    a = Adicionar nome na lista
    r = Remover nome da lista
    m = Obter nome masculino ou feminino
    o = Obter nome para outro tipo de animal
    q = Quantidade de nomes que precisa
    s = Sair 
''')

while executar == True:
    menuPrincipal = input("\n_").lower()
    if menuPrincipal == 'a':
        sexo = input('Digite [M] para masculino e [F] para feminino: ').lower()
        nomeParaAdd = input("Digite o nome: ")
        if sexo == 'm':
            nomesMasculinos.append(nomeParaAdd)
        elif sexo == 'f':
            nomesMasculinos.append(nomeParaAdd)
        else:
            print("Você não definiu o sexo corretamente!")
    elif menuPrincipal == 'r':
        removed = input("Digite o nome que quer remover da lista: ")
        if removed in nomesMasculinos:
            nomesMasculinos.remove(removed)
            print(f'Nome removido com sucesso da lista masculina!')
        elif removed in nomesFeminino:
            nomesFeminino.remove(removed)
            print(f'O nome foi removido com sucesso da lista feminina!')
        else:
            print(f'O nome não está em nenhuma das listas!')
    elif menuPrincipal == 'm':
        sexo2 = input("Qual o sexo do animal? digite [M] para masculno e [f] para feminino: ").lower()
        if sexo2 == 'm':
            print("O nome para seu animal é", choice(nomesMasculinos))
        elif sexo2 == 'f':
            print("O nome para seu animal é", choice(nomesFeminino))
        else:
            print('Você não digitou o sexo corretamente!')
    elif menuPrincipal == 'o':
        sexo3 = input("Qual o sexo do animal? digite [M] para masculno e [f] para feminino: ").lower()
        if sexo3 == 'm':
            print('O nome do seu animal é', choice(nomes_p_qualquer_animal_maculino))
        elif sexo3 == 'f':
            print('O nome do seu animal é', choice(nomes_p_qualquer_animal_feminino))
        else:
            print('Você não digitou o sexo corretamente!')
    elif menuPrincipal == 'q':
        qtd = int(input("Digite a quantidade de nomes que precisa: "))
        while contador < qtd:
            print("O nome do seu animal é", choice(nomes_total))
            contador += 1
    elif menuPrincipal == 's':
        print('Finalizado!\nObrigado por ultilizar nosso programa!')
        executar = False















