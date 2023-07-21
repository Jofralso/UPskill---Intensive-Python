from Classes7_7 import *

if __name__=="__main__":
    Inf=[["Ana Pinto", 14, 15],["Rui Pinto", 17, 18],["Carla Silva", 14, 10],["Telmo Gomes", 10, 12]]
    Pauta = {}
    for a in Inf:
        E=EstudanteInf(a[0], a[1], a[2])
        Pauta[E.Nome]=E.ClassFinal()
    print(Pauta)
