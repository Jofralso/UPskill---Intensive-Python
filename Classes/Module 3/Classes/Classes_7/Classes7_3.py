import math

class EstudanteInf():
    def __init__(self, N, T1, T2):
        self.__Nome = N
        self.__Teste1 = T1
        self.__Teste2 = T2
    
    def getNome(self):
        return self.__Nome
    
    def setNome(self,N):
        self.__Nome = N
    
    def getTeste1(self):
        return self.__Teste1
    
    def setTeste1(self,T1):
        self.__Teste1=T1
    
    def getTeste2(self):
        return self.__Teste2
    
    def setTeste2(self,T2):
        self.__Teste2=T2
    
    def ClassFinal(self):

        return math.floor((self.__Teste1 + self.__Teste2) / 2 + 0.5)

if __name__=="__main__":
    E=EstudanteInf("Ana Paiva", 14, 16)
    E.setNome("Ana G. Paiva")
    E.setTeste1(13)
    E.setTeste2(13)

    print(f"{'Nome':^15}{'Teste 1':^10}{'Teste 2':^10}{'Classif. Final':^15}")
    print(f"{E.getNome():<15}{E.getTeste1():^10}{E.getTeste2():^8}{E.ClassFinal():^16}")
