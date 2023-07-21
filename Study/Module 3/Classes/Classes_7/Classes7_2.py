import math

class EstudanteInf():
    def __init__(self, N, T1, T2):
        self.__Nome = N
        self.__Teste1 = T1
        self.__Teste2 = T2
    
    def getNome(self):
        return self.__Nome
    
    def getTeste1(self):
        return self.__Teste1
    
    def getTeste2(self):
        return self.__Teste2
    
    def ClassFinal(self):

        return math.floor((self.__Teste1 + self.__Teste2) / 2 + 0.5)

if __name__=="__main__":
    E=EstudanteInf("Ana Paiva", 14, 16)
    B=EstudanteInf("Antonio Oliveira", 13, 16)
    C=EstudanteInf("Maria Cunha", 14, 12)
    D=EstudanteInf("José Antunes", 14, 11)

    print(f"{'Nome':^15}{'Teste 1':^10}{'Teste 2':^10}{'Classif. Final':^15}")
    print(f"{E.getNome():<15}{E.getTeste1():^10}{E.getTeste2():^8}{E.ClassFinal():^16}")
    print(f"{B.getNome():<15}{B.getTeste1():^10}{B.getTeste2():^8}{B.ClassFinal():^16}")
    print(f"{C.getNome():<15}{C.getTeste1():^10}{C.getTeste2():^8}{C.ClassFinal():^16}")
    print(f"{D.getNome():<15}{D.getTeste1():^10}{D.getTeste2():^8}{D.ClassFinal():^16}")