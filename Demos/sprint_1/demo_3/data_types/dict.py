def dict_fundamentals():
    print("Fundamentos de dicionários")
    #   Dict: um dado que contéma chave/valor
    
    #   Literal
    my_dict = {
        "modulo": 5
    }
    
    #   Builtin
    my_dict_2 = dict(modulo = 5, instrutores = ["Gustavo", "Lucira"])
    # print(my_dict)
    # print(my_dict_2)
    

    # print(my_dict_2["modulo"])
    # print(my_dict_2["instrutores"])
    
    my_dict_2["instrutores"] = ["Gustavo", "Lucira", "Pedro"]
    # my_dict_2.update({"id": 1})
    my_dict_2.update({"instrutores": ["Jéssica"]})
    print(my_dict_2)
    
    
    #   Looping

def dict_looping():
    my_dict = {
        "modulo": 5 ,
        "instrutores": [ "Lucira", "Gustavo"]
    }
    
    # for chave in my_dict:
    #     print(my_dict[chave])
    #     print(my_dict["modulo"])
    
    # for chave in my_dict.items(): # No JavaScript = Object,entries()
    #     print(chave, valor)

#   Pegar somente as chaves: keys -> my_dict.keys()
    print(my_dict.keys())
#   Pegar somente os valores: keys -> my_dict.values()
    # print(my_dict.values())
