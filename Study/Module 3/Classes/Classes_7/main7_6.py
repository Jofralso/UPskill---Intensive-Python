import math
from Classes7_6 import *

if __name__ == "__main__":
    E=EstudanteInf("Ana Paiva", 14, 16)

    E.Nome=input("Digite o nome correto da aluna: ")
    E.Teste1=int(input(f"Digite a nota do teste 1 da aluna {E.Nome}: "))
    E.Teste2=int(input(f"Digite a nota do teste 2 da aluna {E.Nome}: "))
    
    E.Impressao()