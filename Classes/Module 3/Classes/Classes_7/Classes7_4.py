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

if __name__=="__main__":

    E=EstudanteInf("Ana Paiva", 14, 16)

    E.Nome=input("Digite o nome correto da aluna: ")
    E.Teste1=int(input(f"Digite a nota do teste 1 da aluna {E.Nome}: "))
    E.Teste2=int(input(f"Digite a nota do teste 2 da aluna {E.Nome}: "))
    
    print(f"{'Nome':^15}{'Teste 1':^10}{'Teste 2':^10}{'Classif. Final':^15}")
    print(f"{E.Nome:<15}{E.Teste1:^10}{E.Teste2:^8}{E.ClassFinal():^16}")
