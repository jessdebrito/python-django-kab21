
""" from .operacoes_matematicas.soma import somar # importação relativa"""
from operacoes_matematicas import somar # importação absoluta

print(F"arquivo main: {__name__}")
if __name__ == "__main__": #geralmente aparece desta forma
    somar.soma(1,3)

    