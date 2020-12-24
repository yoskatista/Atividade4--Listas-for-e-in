#Criando listas e executando com o For e In: PG93
lista = str(input('Digite algo que goste para criarmos uma lista'))
lista2 = str(input('Digite mais um item que curta bastante!'))
lista3 = str(input('Agora digite o ultimo item'))
Conjunto = lista, lista2, lista3
for Conjuntos in Conjunto:
    print(Conjuntos)

#Armazenar uma frase para cada item dentro do conjunto 
print('\nO primeiro da lista é o {}, já o segundo é {} e o terceiro...{}. Obrigado'.format(Conjunto[0],Conjunto[1],Conjunto[2]))


#Criando outra lista 
Animal = str(input('Agora Digite um animal que ama:'))
Animal2 = str(input('Digite outro animal:'))
Animal3 = str(input('Digite um ultimo animal'))
Animais = [Animal, Animal2, Animal3]
print('Os animais escolhidos foram {}, {} e {}\nSempre cuide da natureza!'.format(Animais[0],Animais[1],Animais[2]))
