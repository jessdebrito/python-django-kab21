def list_fundamentals():
    print("Fundamentos de Lista")
    #   Lista: conjunto de dados mutaveis de diversos valores/itens
    #   Forma literal
    my_list = [1, 2, 3, "abc", 2.54, ["cde", 8, 9]]
    #   Função builtin. Bultin = nativo
    my_list_2 = list("abc")
    
    print(my_list)
    print(my_list_2)
    
    print(my_list[2])
    my_list.append("test append")
    
def list_looping():
    my_list = [1, 2, 3, "abc", 2.54, ["cde", 8, 9]]
    
    # for item in my_list:
        # print(item)
    
    # print(len(my_list))
    
    # for item in range(5):
    #     print("Hello")

    # for item in range(len(my_list)):
    #     print("oi")
    
    # enumerate numera cada item da lista
    print(len(my_list))
    # for item in enumerate(my_list):
    for indice, valor in enumerate(my_list):
        print(indice, valor)
    