# args -> arguments: não limitar a qtd de parâmetros simples que vai ser recebido
# def somar_salarios(a: float, b: float, c: float, d: float) -> float:
#     return a + b + c + d

def recebe_args(*args: tuple):
    return args


def somar_salarios(*args: tuple) -> float:
    # print(args)
    # print(type(args))
    for arg in args:
        if type(arg) != float:
            # return "Valor errado. Mande somente números com ponto flutuante"
            message = (
                "Você mandou números inteiros."
                "Envie somente números com pontos flutuantes."
            )
            # throw new ValueError
            raise ValueError(message) # Levantamento de exceção
    resultado = sum(args)
    return resultado
    # Try/Catch
    # try: # tratamento de exceção
    #     resultado = sum(args)
    #     # TypeError
    # except: # Má prática
    #     return "Valor errado. Mande somente números com ponto flutuante"

    # try:
    #     from screen import a
    #     resultado = sum(args)
    #     # TypeError
    # except TypeError: # recomendado
    #     return "Valor errado. Mande somente números com ponto flutuante"
    # except ModuleNotFoundError: # recomendado
    #     return "Você está tentando importar algo que não existe."
    # return resultado


def media_salarios(*args: tuple) -> float:
    # Média: somando todos os valores e depois, divide o resultado pelo qtd de valores
    print(args)
    resultado = somar_salarios(*args) # (2000.5, 1250.4) -> 2000.5, 1250.4
    media = resultado / len(args)
    return media


# kwargs -> keyword arguments: não limita a qtd de parâmetros nomeados que vão ser recebidos

def mostrar_dados_pessoais(**kwargs: dict):
    print(kwargs)
    print(type(kwargs))
    return kwargs