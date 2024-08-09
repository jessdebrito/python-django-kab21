#           Declaração de variável
# Padrão de nomenclatura snake case = acada fim de palavra usar o _
""" minha_variavel = "string"
minha_variavel_2 = 1
minha_variavel_3 = 2.5
minha_variavel_4 = [1, 2, 3] # Lista |  Js é chamado de array
minha_variavel_5 = { "modulo": 5, "instrutores": ["Lucira", " Gustavo"]} # Dicionário | Js = objeto
 """
#           Function:
# def minha_funcao():
    # print("Hello") # concole.log() -> demonstra a saida

# minha_funcao()
# print("Hello World!")
# print("fora da function")

#         Condicional 
""" minha_variavel = 5
if minha == 5:
    print("Minha variável tem valor de 5")
elif minha_variavel == 10:                 # elif = if else
    print("Minha variável tem valor de 10")
else:
    print("Minha variável não tem valor de 5") """

""" minha_variavel = 10
if minha == 7:
    print(f"Minha variável tem valor de {minha_variavel}")
elif minha_variavel == 10:                 # elif = if else
    print("Minha variável tem valor de 10")
else:
    print("Minha variável não tem valor de 5") """

#       Tipagem
""" minha_string: str = "abc" # type hit -> dicas de tipagem. Diferente do TypeScript, não acusa erro
print(minha_string) """

# def minha_funcao(a: int, b: str) -> str:
""" def minha_funcao() -> str:
    return ("oi")
 """
#    Ternários não tem em Py, mas existe algo parecido:
""" ------ JavaScript:
double salario = 1000; 
double bonus = salario * (salario > 1000 ? 0.10 : 0.15); 
System.out.println(bonus); """

""" minha_variavel = 13
teste = "par" if minha_variavel == 2 else "impar"
print(teste) """

#       Estrutura de repetição numa lista
""" minha_lista = [1, 2, 3] # Lista
# for number in minha_lista:
#     print(number)
iterador = 0
# len -> length
while iterador < len(minha_lista):
    print(minha_lista[iterador])
    iterador += 1 """

#          
meu_dicionario = { "modulo": 5, "instrutores": ["Lucira", " Gustavo"]}
""" for chave in meu_dicionario:
    print(chave)
    # Quando percorre um dicionário, só tem acesso as chaves """

    # No JS: meu_objeto.chave, meu_objeto.moculo, meu_objeto.instrutores
""" print(meu_dicionario["modulo"])
print(meu_dicionario["instrutores"]) """
for chave in meu_dicionario:
            print*meu_dicionario