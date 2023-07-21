import math

class EstudanteInf():
    def __init__(self, N, T1, T2):
        self.__Nome = N
        self.__Teste1 = T1
        self.__Teste2 = T2

#NOTA: em ambos os def deixa de ter 'set' e 'get' 
#Passa a (self,N) e igualamos a N

    @property
    def Nome(self):
        return self.__Nome    
    
    @Nome.setter
    def Nome(self,N):
        self.__Nome = N

    @property 
    def Teste1(self):
        return self.__Teste1
    
    @Teste1.setter
    def Teste1(self,N):
        self.__Teste1 = N

    @property
    def Teste2(self):
        return self.__Teste2
    
    @Teste2.setter
    def Teste2(self,N):
        self.__Teste2 = N

    def ClassFinal(self):
        return math.floor((self.__Teste1 + self.__Teste2) / 2 + 0.5)

    def Impressao(self):
        print(f"{'Nome':^15}{'Teste 1':^10}{'Teste 2':^10}{'Classif. Final':^15}")
        print(f"{self.Nome:<15}{self.Teste1:^10}{self.Teste2:^8}{self.ClassFinal():^16}")
        return
    