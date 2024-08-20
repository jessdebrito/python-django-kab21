from pessoas.gerenciamento import (
    somar_salarios, 
    media_salarios, 
    mostrar_dados_pessoais,
    recebe_args
    )

if __name__ == "__main__":
    # print(somar_salarios(2000.50, 1250.4))
    # print(somar_salarios(1, 2, 2))
    # print(media_salarios(2000.50, 1250.4))
    # print(
    #     mostrar_dados_pessoais(
    #         nome="Lucira", ultimo_nome="Silva",
    #         estado="AP", telefone=1235567789
    #     )
    # )

    # dicionario = {
    #     "nome": "Lucira",
    #     "ultimo_nome": "Silva",
    #     "telefone": 1235567789
    # }


    # print(
    #     mostrar_dados_pessoais(**dicionario)
    # )
    # lista = [5, 213.5]

    # print(recebe_args(*lista))
    # print(somar_salarios(1, 1200, 5))
    # print(20.3f) # 20.000
    
    print(round(20.10, 2))