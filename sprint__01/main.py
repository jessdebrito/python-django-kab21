# #            Loop        # # 
# # imprime cada elemento da lista
#for numero in [1, 2, 3]:
#    print(numero)

# # imprime cada caractere da string
#for caractere in "Olá, mundo!":
#    print(caractere)



# # imprimindo os números de 1 a 5
#for i in range (1, 6):
#    print(i)

# # imprimindo os números de 1 a 5
#i = 1
#while 1 <= 5:
#    print(i)
#    i += 1
#print(i)


# # imprimindo os números de 1 a 5, mas interrompe o loop quando o número é
#for i in range (1, 6):
#    if i == 3:
#        break
#    print(i)

# # imprimindo os números de 1 a 5, mas interrompe o loop quando o número é
#for i in range (1, 6):
#    if i == 3:
#       continue
#    print(i)


# #            Dicionário        # #
#my_dictionary = {}
#type(my_dictionary)

#my_dictionary = {'chave': 'valor'}
#print(my_dictionary)

#my_dictionary['chave']


# # Para criar um dicionário, basta indicar os valores e usar o dict:
#>>> my_dictionary = dict(chave="valor")
#>>> my_dictionary
    #{'chave': 'valor'}


# # Para criar vários itens para o dicionário de uma vez: 
# my_dictionary = dict([('primeiro', 1,) , ('segundo', 2,), ('terceiro',3,)])
# >>> my_dictionary
    # {'primeiro': 1, 'segundo': 2, 'terceiro': 3}

# # Relacionando listas. Sendo relacionado o primeiro elemento da lista 1, com o primeiro da lista 2. E assim segue...
# lista_1 = ['primeiro', 'segundo', 'terceiro']
# lista_2 = [1,2,3]
# my_dictionary = dict(zip(lista_1, lista_2))
    # {'primeiro': 1, 'segundo': 2, 'terceiro': 3}

# # Cria um dicionário com uma lista de chaves, e usará apenas um valor
#chaves = ['primeiro', 'segundo', 'terceiro']
#valor = 0
#my_dictionary = dict.fromkeyskeys(chaves, valor)
        # {'primeiro': 0, 'segundo': 0, 'terceiro': 0}


        # #    Acessar elementos dos dicionários
# my_dictionary = dict(primeiro=1, segundo=2, terceiro='terceiro')
    # {'primeiro': 1, 'segundo': 2, 'terceiro': 'terceiro'}
    # my_dictionary['segundo']
    # 2

    # my_dictionary.get('segundo')
    # 2

        # #    Retornar apenas as chaves do dicionário
        # {'primeiro': 1, 'segundo': 2, 'terceiro': 'terceiro'}
        #my_dictionary.keys()
        #dict_keys({'primeiro', 'segundo', 'terceiro'})

